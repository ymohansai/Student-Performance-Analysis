import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
DATA_PATH = os.path.join("data", "student-mat.csv") 
OUTPUTS_DIR = "outputs"
os.makedirs(OUTPUTS_DIR, exist_ok=True)
print("Loading dataset...")
df = pd.read_csv(DATA_PATH, sep=";") 
print("Dataset loaded")
print("Shape:", df.shape)
print(df.head(), "\n")
print("Checking nulls and duplicates...")
print("Missing values:", df.isnull().sum().sum())
print("Duplicates:", df.duplicated().sum())
if df.duplicated().sum() > 0:
    df = df.drop_duplicates().reset_index(drop=True)
    print(" Duplicates removed. New shape:", df.shape)
print("\n Analysis:")
avg_g3 = df["G3"].mean()
print(f"1) Average final grade (G3): {avg_g3:.2f}")
above_15 = (df["G3"] > 15).sum()
print(f"2) Students scoring above 15: {above_15} out of {len(df)}")
spearman_corr = df["studytime"].corr(df["G3"], method="spearman")
pearson_corr = df["studytime"].corr(df["G3"], method="pearson")
print(f"3) Correlation studytime vs G3 → Spearman: {spearman_corr:.3f}, Pearson: {pearson_corr:.3f}")
gender_avg = df.groupby("sex")["G3"].mean().rename({"F": "Female", "M": "Male"})
print("4) Average grade by gender:\n", gender_avg, "\n")
plt.figure()
df["G3"].plot(kind="hist", bins=21, edgecolor="black")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Count")
plt.title("Distribution of Final Grades")
plt.savefig(os.path.join(OUTPUTS_DIR, "hist_grades.png"), dpi=150)
plt.close()
plt.figure()
jitter = np.random.uniform(-0.1, 0.1, size=len(df))
plt.scatter(df["studytime"] + jitter, df["G3"], alpha=0.6)
plt.xticks([1,2,3,4], ["<2h","2-5h","5-10h",">10h"])
plt.xlabel("Study Time Category")
plt.ylabel("Final Grade (G3)")
plt.title("Study Time vs Final Grade")
plt.savefig(os.path.join(OUTPUTS_DIR, "scatter_studytime.png"), dpi=150)
plt.close()
plt.figure()
avg_by_sex = df.groupby("sex")["G3"].mean().rename({"F": "Female", "M": "Male"})
avg_by_sex.plot(kind="bar", color=["skyblue", "orange"])
plt.xlabel("Gender")
plt.ylabel("Average Final Grade")
plt.title("Average G3 by Gender")
plt.savefig(os.path.join(OUTPUTS_DIR, "bar_gender.png"), dpi=150)
plt.close()
print("Visualizations saved in 'outputs/' folder")
cleaned_csv = os.path.join(OUTPUTS_DIR, "student-mat_clean.csv")
df.to_csv(cleaned_csv, index=False)
cleaned_xlsx = os.path.join(OUTPUTS_DIR, "student-mat.xlsx")
df.to_excel(cleaned_xlsx, index=False)
summary = f"""
Student Performance Analysis - Task 1
1) Average final grade (G3): {avg_g3:.2f}
2) Students scoring above 15: {above_15} / {len(df)}
3) Studytime correlation with G3:
   Spearman = {spearman_corr:.3f}, Pearson = {pearson_corr:.3f}
4) Average grade by gender:
{gender_avg.to_string()}
"""
with open(os.path.join(OUTPUTS_DIR, "summary.txt"), "w", encoding="utf-8") as f:
    f.write(summary.strip())
print("Outputs saved: cleaned CSV, Excel, summary.txt, and charts in outputs/")

