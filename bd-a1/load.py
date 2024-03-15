import sys
import pandas as pd
import subprocess


file_path = sys.argv[1]

df = pd.read_csv(file_path)  

print(df.head())

subprocess.run(["python3", "dpre.py", file_path])
