from src.scoring import hybrid_score
from src.utils import preprocess
import pandas as pd
import os
import pandas as pd

input_file = "data/AutoEIT Sample Transcriptions for Scoring.xlsx"
output_folder = "output"
os.makedirs(output_folder, exist_ok=True) 
output_file = os.path.join(output_folder, "final_output.xlsx")
xls = pd.ExcelFile(input_file)
with pd.ExcelWriter(output_file) as writer:
    for sheet in xls.sheet_names[1:]: 
        df = pd.read_excel(xls, sheet_name=sheet)
        
        #apply preprocessing 
        df["clean_stimulus"] = df["Stimulus"].apply(preprocess)
        df["clean_original"] = df["Transcription Rater 1"].apply(preprocess)
        
        #apply hybrid score row-wise
        df["Score"] = df.apply(
            lambda row: hybrid_score(row["clean_stimulus"], row["clean_original"]), axis=1
        )
        df.to_excel(writer, sheet_name=sheet, index=False)
print(f"All sheets processed and saved to {output_file}")