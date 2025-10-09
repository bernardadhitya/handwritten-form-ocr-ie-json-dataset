#!/usr/bin/env python3
"""
Git Batch Commit Script
Handles adding, committing, and pushing untracked files in batches of 20.
"""

import subprocess
import sys
import os
import time
from datetime import datetime
from typing import List, Tuple

class GitBatchCommiter:
    def __init__(self, batch_size: int = 20, log_file: str = "git_batch_commit.log"):
        self.batch_size = batch_size
        self.log_file = log_file
        self.total_files = 0
        self.processed_files = 0
        self.batch_number = 0
        
    def log_message(self, message: str):
        """Log message to both console and log file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
    
    def run_git_command(self, command: List[str]) -> Tuple[bool, str]:
        """Run a git command and return success status and output"""
        try:
            result = subprocess.run(
                command, 
                capture_output=True, 
                text=True, 
                check=True,
                cwd=os.getcwd()
            )
            return True, result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return False, e.stderr.strip()
    
    def get_untracked_files(self) -> List[str]:
        """Get list of all untracked files"""
        success, output = self.run_git_command(["git", "status", "--porcelain"])
        if not success:
            self.log_message(f"Error getting git status: {output}")
            return []
        
        untracked_files = []
        for line in output.split('\n'):
            if line.startswith('??'):
                # Remove the '?? ' prefix and get the file path
                file_path = line[3:].strip()
                # Handle quoted paths (for paths with spaces)
                if file_path.startswith('"') and file_path.endswith('"'):
                    file_path = file_path[1:-1]
                untracked_files.append(file_path)
        
        return untracked_files
    
    def get_all_files_recursive(self, directories: List[str]) -> List[str]:
        """Get all files recursively from given directories"""
        all_files = []
        for directory in directories:
            if os.path.isdir(directory):
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        file_path = os.path.join(root, file)
                        all_files.append(file_path)
        return all_files
    
    def add_files_to_git(self, files: List[str]) -> bool:
        """Add files to git staging area"""
        if not files:
            return True
            
        # Use git add with multiple file paths
        command = ["git", "add"] + files
        success, output = self.run_git_command(command)
        
        if success:
            self.log_message(f"Successfully added {len(files)} files to staging area")
        else:
            self.log_message(f"Error adding files: {output}")
        
        return success
    
    def commit_files(self, batch_num: int) -> bool:
        """Commit staged files with batch message"""
        commit_message = f"Add batch {batch_num:03d} - {len(self.get_staged_files())} files"
        command = ["git", "commit", "-m", commit_message]
        success, output = self.run_git_command(command)
        
        if success:
            self.log_message(f"Successfully committed batch {batch_num}")
        else:
            self.log_message(f"Error committing batch {batch_num}: {output}")
        
        return success
    
    def get_staged_files(self) -> List[str]:
        """Get list of currently staged files"""
        success, output = self.run_git_command(["git", "diff", "--cached", "--name-only"])
        if not success:
            return []
        return [line.strip() for line in output.split('\n') if line.strip()]
    
    def push_to_main(self) -> bool:
        """Push commits to main branch"""
        command = ["git", "push", "origin", "main"]
        success, output = self.run_git_command(command)
        
        if success:
            self.log_message("Successfully pushed to main branch")
        else:
            self.log_message(f"Error pushing to main: {output}")
        
        return success
    
    def check_unpushed_commits(self) -> List[str]:
        """Check for commits that haven't been pushed to origin/main"""
        command = ["git", "log", "--oneline", "origin/main..HEAD"]
        success, output = self.run_git_command(command)
        
        if success and output:
            commits = [line.strip() for line in output.split('\n') if line.strip()]
            self.log_message(f"Found {len(commits)} unpushed commits:")
            for commit in commits:
                self.log_message(f"  {commit}")
            return commits
        elif success and not output:
            self.log_message("No unpushed commits found")
            return []
        else:
            self.log_message(f"Error checking unpushed commits: {output}")
            return []
    
    def show_git_status(self):
        """Show current git status and unpushed commits"""
        self.log_message("=== Git Status ===")
        
        # Show git status
        success, output = self.run_git_command(["git", "status", "--short"])
        if success:
            if output:
                self.log_message("Current git status:")
                for line in output.split('\n'):
                    if line.strip():
                        self.log_message(f"  {line}")
            else:
                self.log_message("Working directory is clean")
        
        # Show unpushed commits
        self.log_message("=== Unpushed Commits ===")
        unpushed = self.check_unpushed_commits()
        
        return len(unpushed) > 0
    
    def process_batch(self, files: List[str]) -> bool:
        """Process a single batch of files"""
        self.batch_number += 1
        
        self.log_message(f"Processing batch {self.batch_number} with {len(files)} files")
        
        # Add files to git
        if not self.add_files_to_git(files):
            return False
        
        # Commit the batch
        if not self.commit_files(self.batch_number):
            return False
        
        # Push to main
        if not self.push_to_main():
            return False
        
        self.processed_files += len(files)
        self.log_message(f"Batch {self.batch_number} completed. Progress: {self.processed_files}/{self.total_files} files processed")
        
        return True
    
    def run(self):
        """Main execution function"""
        self.log_message("Starting git batch commit process")
        self.log_message(f"Batch size: {self.batch_size}")
        
        # Get all untracked files
        all_files = self.get_untracked_files()
        self.total_files = len(all_files)
        self.log_message(f"Found {self.total_files} untracked files")
        
        self.log_message(f"Total files to process: {self.total_files}")
        
        if self.total_files == 0:
            self.log_message("No files to process. Exiting.")
            return
        
        # Process files in batches
        for i in range(0, len(all_files), self.batch_size):
            batch = all_files[i:i + self.batch_size]
            
            self.log_message(f"Starting batch {self.batch_number + 1} ({len(batch)} files)")
            
            if not self.process_batch(batch):
                self.log_message(f"Failed to process batch {self.batch_number}. Stopping.")
                break
            
            # Small delay between batches to avoid overwhelming the system
            time.sleep(1)
        
        self.log_message(f"Batch commit process completed. Processed {self.processed_files}/{self.total_files} files in {self.batch_number} batches")

def main():
    """Main function"""
    batch_size = 20
    check_status = False
    
    # Parse command line arguments
    for arg in sys.argv[1:]:
        if arg == "--status" or arg == "-s":
            check_status = True
        elif arg.isdigit():
            batch_size = int(arg)
        elif arg in ["--help", "-h"]:
            print("Usage: python3 git_batch_commit.py [batch_size] [--status]")
            print("  batch_size: Number of files to process per batch (default: 20)")
            print("  --status, -s: Check git status and show unpushed commits")
            print("  --help, -h: Show this help message")
            return
    
    commiter = GitBatchCommiter(batch_size=batch_size)
    
    if check_status:
        commiter.show_git_status()
    else:
        commiter.run()

if __name__ == "__main__":
    main()
