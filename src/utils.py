import pandas as pd 
import numpy as np
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher

file_path="data/AutoEIT Sample Transcriptions for Scoring.xlsx"
xls = pd.ExcelFile(file_path)
sheet_names = xls.sheet_names
df=pd.read_excel(xls,sheet_name=sheet_names[1])

def preprocess(text):
    if pd.isna(text):
        return "";
    text=text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text=re.sub(r'[^\w\s]','',text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
df["clean_stimulus"]=df["Stimulus"].apply(preprocess)
df["clean_original"]=df["Transcription Rater 1"].apply(preprocess)

def word_overlap(s1, s2):
    set1 = set(s1.split())
    set2 = set(s2.split())
    if len(set1) == 0:
        return 0
    return len(set1 & set2) / len(set1)

model=SentenceTransformer('all-MiniLM-L6-v2')

def semantic(s1,s2):
    emb1=model.encode(s1)
    emb2=model.encode(s2)
    sim=cosine_similarity([emb1],[emb2])[0][0]
    return sim

def edit_sim(s1,s2):
    return SequenceMatcher(None,s1,s2).ratio()

def missing_word(s1,s2):
    word1=set(s1.split())
    word2=set(s2.split())
    missing=len(word1-word2)
    return missing/len(word1)

def get_ngrams(text, n):
    words = text.split()
    return [" ".join(words[i:i+n]) for i in range(len(words)-n+1)]

def ngram_overlap(s1, s2, n=2):
    ngrams1 = set(get_ngrams(s1, n))
    ngrams2 = set(get_ngrams(s2, n))
    if len(ngrams1) == 0:
        return 0
    return len(ngrams1 & ngrams2) / len(ngrams1)

def length_ratio(s1, s2):
    if len(s1.split()) == 0:
        return 0
    return len(s2.split()) / len(s1.split())



