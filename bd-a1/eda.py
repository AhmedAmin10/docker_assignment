import sys
import pandas as pd
import subprocess as run

# file_path = sys.argv[1]

df = pd.read_csv('wc.csv')

# First EDA
with open('eda-in-1.txt', 'w') as file:
    file.write(df.describe().to_string())

# Second EDA
correlation_matrix = df[["Age", "Rating", "Recommended IND", "Positive Feedback Count"]].corr()
with open('eda-in-2.txt', 'w') as file:
    file.write("Correlation Matrix:\n" + correlation_matrix.to_string())

# Third EDA
skewness = df[["Age", "Rating", "Recommended IND", "Positive Feedback Count"]].skew()
kurtosis = df[["Age", "Rating", "Recommended IND", "Positive Feedback Count"]].kurtosis()
with open('eda-in-3.txt', 'w') as file:
    file.write("Skewness:\n" + skewness.to_string() + "\n\nKurtosis:\n" + kurtosis.to_string())

print("Successful Execution eda.py")

run(["python3", "vis.py", 'res_dpre.csv'])
