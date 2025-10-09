# Handwritten Form OCR Information Extraction Dataset

## Overview

This repository contains a comprehensive collection of handwritten form images sourced from various datasets, each accompanied by OCR-scanned text and structured JSON representations. The dataset is designed to support research and development in Optical Character Recognition (OCR), Information Extraction (IE), and handwritten text analysis applications.

## Dataset Sources

The collection includes images from the following well-known datasets:

### 1. FUNSD (Form Understanding in Noisy Scanned Documents)
FUNSD is a dataset for form understanding in noisy scanned documents, containing 199 real, fully annotated, scanned forms with 30,000+ semantic entities. The dataset includes various types of forms such as administrative documents, surveys, and questionnaires, making it valuable for form understanding and information extraction research.

| 0000990274.png | 0001123541.png | 0001463282.png |
|:---:|:---:|:---:|
| ![FUNSD Sample 1](src/0000990274.png) | ![FUNSD Sample 2](src/0001123541.png) | ![FUNSD Sample 3](src/0001463282.png) |

### 2. IAM (IAM Handwriting Database)
The IAM Handwriting Database is a large dataset containing handwritten English text from various writers. It includes forms of handwritten English text, which are useful for training and testing handwriting recognition systems. The database contains both isolated words and complete sentences, providing diverse handwriting styles and complexity levels.

| a01-000u.png | a01-003u.png | a01-007u.png |
|:---:|:---:|:---:|
| ![IAM Sample 1](src/a01-000u.png) | ![IAM Sample 2](src/a01-003u.png) | ![IAM Sample 3](src/a01-007u.png) |

### 3. RVL-CDIP (Ryerson Vision Lab Complex Document Information Processing)
RVL-CDIP is a dataset for document classification and information extraction, containing 400,000 grayscale images in 16 classes. The dataset includes various document types including forms, making it suitable for document understanding and classification tasks.

| 500022678.tif | 500083831_500083835.tif | 500183719_500183721.tif |
|:---:|:---:|:---:|
| ![RVL-CDIP Sample 1](src/500022678.png) | ![RVL-CDIP Sample 2](src/500083831_500083835.png) | ![RVL-CDIP Sample 3](src/500183719_500183721.png) |

### 4. RIMES (Reconnaissance et Indexation de données Manuscrites et de fac similÉS)
RIMES is a French handwriting recognition dataset containing handwritten mail documents. It includes various types of handwritten correspondence and forms, providing a rich resource for French handwriting recognition and document analysis.

| 00001_L.tif | 00002_L.tif | 00003_L.tif |
|:---:|:---:|:---:|
| ![RIMES Sample 1](src/00001_L.png) | ![RIMES Sample 2](src/00002_L.png) | ![RIMES Sample 3](src/00003_L.png) |

### 5. CVL Database
The CVL Database is a handwriting recognition dataset containing handwritten text from multiple writers. It provides a diverse collection of handwritten documents suitable for training and evaluating handwriting recognition systems.

| 0001-1.tif | 0001-2.tif | 0001-3.tif |
|:---:|:---:|:---:|
| ![CVL Sample 1](src/0001-1.png) | ![CVL Sample 2](src/0001-2.png) | ![CVL Sample 3](src/0001-3.png) |

### 6. IDRBT Cheque Image Dataset
This dataset contains bank cheque images with various handwriting styles and formats. It's particularly useful for financial document processing and bank form analysis applications.

| Cheque 083654.tif | Cheque 083655.tif | Cheque 083656.tif |
|:---:|:---:|:---:|
| ![IDRBT Sample 1](src/Cheque%20083654.png) | ![IDRBT Sample 2](src/Cheque%20083655.png) | ![IDRBT Sample 3](src/Cheque%20083656.png) |

### 7. 10 Banks Cheque Dataset
A collection of cheque images from 10 different banks (Axis, ICICI, HSBC, Canara, Credit, Biat, Banque, Attihari, Saudi, Universelle), providing diverse banking form formats and handwriting styles for financial document analysis.

| 1.jpg | 2.jpg | 3.jpg |
|:---:|:---:|:---:|
| ![Axis Sample 1](src/1.jpg) | ![Axis Sample 2](src/2.jpg) | ![Axis Sample 3](src/3.jpg) |


## Repository Structure

```
handwritten-form-ocr-ie-json-dataset/
├── Dataset/                          # Original image datasets
│   ├── 10_banks_cheque/             # Bank cheque images
│   ├── cvl-database-1-1/            # CVL database images
│   ├── FUNSD_cleaned/               # FUNSD form images
│   ├── IAM/                         # IAM handwriting database
│   ├── IDRBT_Cheque_Image_Dataset/  # IDRBT cheque images
│   ├── RIMES_Images_Courriers/      # RIMES mail images
│   └── RVL_CDIP small/              # RVL-CDIP document images
├── OCR_text/                        # OCR extracted text files
│   ├── 10_banks_cheque/             # OCR text for bank cheques
│   ├── cvl-database-1-1/            # OCR text for CVL database
│   ├── FUNSD_cleaned/               # OCR text for FUNSD forms
│   ├── IAM/                         # OCR text for IAM database
│   ├── IDRBT_Cheque_Image_Dataset/  # OCR text for IDRBT cheques
│   ├── RIMES_Images_Courriers/      # OCR text for RIMES mail
│   └── RVL_CDIP small/              # OCR text for RVL-CDIP documents
├── JSON_file/                       # Structured JSON representations
│   ├── 10_banks_cheque/             # JSON for bank cheques
│   ├── cvl-database-1-1/            # JSON for CVL database
│   ├── FUNSD_cleaned/               # JSON for FUNSD forms
│   ├── IAM/                         # JSON for IAM database
│   ├── IDRBT_Cheque_Image_Dataset/  # JSON for IDRBT cheques
│   ├── RIMES_Images_Courriers/      # JSON for RIMES mail
│   ├── RVL_CDIP small/              # JSON for RVL-CDIP documents
│   └── test_accuracy/               # Test accuracy evaluation files
└── README.md                        # This file
```

## Data Format

### Images
- **Format**: Various formats (PNG, TIF, JPG)
- **Content**: Handwritten forms, cheques, documents, and correspondence
- **Quality**: Scanned documents with varying quality and noise levels

### OCR Text Files
- **Format**: Plain text (.txt)
- **Content**: Raw OCR output from the corresponding images
- **Encoding**: UTF-8

### JSON Files
- **Format**: JSON (.json)
- **Content**: Structured representation of extracted information
- **Structure**: Varies by dataset type:
  - **Bank Cheques**: Contains fields like bank name, date, payee, amount, account number, etc.
  - **Forms**: Contains structured form fields and their values
  - **General Documents**: Contains document metadata and extracted text

## Usage Examples

### Bank Cheque Example
**Image**: `src/1.jpg`
**OCR Text**: `OCR_text/10_banks_cheque/Axis/1.txt`
**JSON**: `JSON_file/10_banks_cheque/Axis/1.json`
```json
{
    "bank": "AXIS BANK",
    "date": "060522",
    "validFor": "THREE",
    "payee": "Edmee Pelletier",
    "currency": "RUPEE",
    "amountInWords": "Three Thousand Seven Hundred and Fifty Five",
    "amount": 3755,
    "accountNumber": "59480450090495004985",
    "transactionCode": "SAM426160",
    "branchCode": "000001",
    "referenceNumber": "50020242616031"
}
```

### Form Example (FUNSD)
**Image**: `src/0000990274.png`
**OCR Text**: `OCR_text/FUNSD_cleaned/0000990274.txt`
**JSON**: `JSON_file/FUNSD_cleaned/0000990274.json`
```json
{
    "serviceRequest": {
        "from": "R&D",
        "by": "2AM8",
        "requestNo": "25-84",
        "receivedDate": "April 2, 1984",
        "date": "",
        "initiatedBy": {
            "initials": "P.H.H.",
            "name": "P.E. Harper"
        },
        "completionTargetDate": "April 13, 1984",
        "country": "Belgium",
        "product": [
            "Lucky Strike Filter",
            "Viceroy"
        ],
        "natureOfWork": "Advise if locally obtained Yucatan Honey (sample enclosed) is an acceptable substitute for HALwAy.",
        "rsdComments": "T-yx7 JA OK.",
        "notes": [
            "Nature of work should be specified in exact terms.",
            "RD should advise if completion date cannot be met.",
            "Two copies of this form to be sent to RsD by initiator and RsD is to return to T.O. one completed copy."
        ],
        "mhEnm": "0036/r",
        "code": "2894M",
        "reference": "620429480"
    }
}
```

## Applications

This dataset is suitable for:

- **OCR Model Training**: Training and evaluating optical character recognition systems
- **Information Extraction**: Developing systems to extract structured information from forms
- **Document Classification**: Classifying different types of handwritten documents
- **Handwriting Recognition**: Training handwriting recognition models
- **Form Understanding**: Developing systems to understand and process various form types
- **Financial Document Processing**: Processing bank cheques and financial forms
- **Multi-language OCR**: Working with documents in different languages (English, French, etc.)

## File Naming Convention

- **Images**: Original filenames from source datasets
- **OCR Text**: Same filename as image with `.txt` extension
- **JSON**: Same filename as image with `.json` extension

## Dataset Statistics

- **Total Images**: ~50,000+ handwritten form images
- **Languages**: English, French, and other languages
- **Document Types**: Forms, cheques, correspondence, administrative documents
- **Writers**: Multiple writers with diverse handwriting styles
- **Quality**: Varying quality levels from high-resolution scans to noisy documents

## License

This dataset compilation is provided for research and educational purposes. Please refer to the original dataset licenses for specific usage terms:

- **FUNSD**: Available for research use
- **IAM**: Available for research use
- **RVL-CDIP**: Available for research use
- **RIMES**: Available for research use
- **CVL Database**: Available for research use
- **IDRBT**: Available for research use

## Citations

If you use this dataset compilation in your research, please cite the original datasets:

### FUNSD
```
@article{jaume2019funsd,
  title={FUNSD: A Dataset for Form Understanding in Noisy Scanned Documents},
  author={Jaume, Guillaume and Ekenel, Hazim Kemal and Thiran, Jean-Philippe},
  journal={arXiv preprint arXiv:1905.13538},
  year={2019}
}
```

### IAM Handwriting Database
```
@article{marti2002iam,
  title={The IAM-database: an English sentence database for offline handwriting recognition},
  author={Marti, U-V and Bunke, Horst},
  journal={International Journal on Document Analysis and Recognition},
  volume={5},
  number={1},
  pages={39--46},
  year={2002},
  publisher={Springer}
}
```

### RVL-CDIP
```
@article{harley2015evaluation,
  title={Evaluation of deep convolutional nets for document image classification and retrieval},
  author={Harley, Adam W and Ufkes, Andrew and Derpanis, Konstantinos G},
  journal={Proceedings of the 13th International Conference on Document Analysis and Recognition (ICDAR)},
  pages={991--995},
  year={2015}
}
```

### RIMES
```
@inproceedings{grosicki2009rimes,
  title={The RIMES database for handwritten text recognition},
  author={Grosicki, Emmanuel and El-Abed, Haikal},
  booktitle={Proceedings of the 10th International Conference on Document Analysis and Recognition},
  pages={785--789},
  year={2009},
  organization={IEEE}
}
```

### CVL Database
```
@inproceedings{kleber2013cvl,
  title={CVL-database: An off-line database for writer retrieval, writer identification and word spotting},
  author={Kleber, Florian and Fiel, Stefan and Diem, Markus and Sablatnig, Robert},
  booktitle={Proceedings of the 12th International Conference on Document Analysis and Recognition},
  pages={560--564},
  year={2013},
  organization={IEEE}
}
```

### IDRBT Cheque Dataset
```
@article{idrbt_cheque,
  title={IDRBT Cheque Image Dataset},
  author={Institute for Development and Research in Banking Technology},
  journal={Technical Report},
  year={2015}
}
```

## Acknowledgments

We extend our gratitude to the creators and maintainers of the original datasets:

- **FUNSD**: Guillaume Jaume, Hazim Kemal Ekenel, and Jean-Philippe Thiran
- **IAM**: U-V Marti and Horst Bunke
- **RVL-CDIP**: Adam W. Harley, Andrew Ufkes, and Konstantinos G. Derpanis
- **RIMES**: Emmanuel Grosicki and Haikal El-Abed
- **CVL Database**: Florian Kleber, Stefan Fiel, Markus Diem, and Robert Sablatnig
- **IDRBT**: Institute for Development and Research in Banking Technology

## Citation

If you use this dataset in your research, please cite the original datasets appropriately and acknowledge this compilation.

## Contact

For questions or issues related to this dataset compilation, please open an issue in the repository.

---

*This dataset compilation aims to provide a comprehensive resource for handwritten form OCR and information extraction research.*
