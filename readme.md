# AutoEIT Scoring System

This project implements an automated scoring system for EIT (Engineering Interview Test) transcription responses. 
It calculates a hybrid score (0–4) for each response based on:

- Word overlap
- Semantic similarity using Sentence-BERT
- Edit similarity (sequence matching)
- Bigram overlap
- Length ratio
- Missing words

It processes multiple Excel sheets of responses and outputs a scored Excel file.

## Folder Structure
- data/AutoEIT Sample Transcriptions for Scoring.xlsx
- notebook/AutoEIT_Scoring.ipynb
- output/final_output.xlsx
- src/scoring.py
     /utils.py
- main.py
- requirements.txt

## Features

- Preprocesses text (lowercasing, removing punctuation, extra spaces)
- Computes hybrid score per response
- Processes multiple sheets in an Excel file
- Saves results to a single Excel file in the `output/` folder
- Uses `SentenceTransformer` for semantic similarity

## Requirements

Python 3.10+  

Install dependencies using pip:

pip install -r requirements.txt

## How to run

1. Make sure the Excel input file is in `data/` folder.  
2. Activate your virtual environment:
```bash
# Windows
myenv\Scripts\activate

# macOS/Linux
source myenv/bin/activate

# Run main script
python main.py
```
## Notes

- The first sheet of the Excel file is skipped (assumed metadata or instructions).  
- HF Hub warnings about unauthenticated requests are normal for Sentence-BERT.  
  You can set a Hugging Face token for faster downloads:

```bash
set HF_TOKEN=<your_token>  # Windows
export HF_TOKEN=<your_token>  # macOS/Linux
```