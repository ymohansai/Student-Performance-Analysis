import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# 1. Setup paths
# ----------------------------
DATA_PATH = os.path.join("data", "student-mat.csv")   # dataset location
OUTPUTS_DIR = "outputs"
os.makedirs(OUTPUTS_DIR, exist_ok=True)

# ----------------------------
# 2. Load dataset
# ----------------------------
print("📥 Loading dataset...")
df = pd.read_csv(DATA_PATH, sep=";")   # NOTE: file uses ';' as separator

print("✅ Dataset loaded")
print("Shape:", df.shape)
print(df.head(), "\n")

# ----------------------------
# 3. Explore & clean
# ----------------------------
print("🔎 Checking nulls and duplicates...")
print("Missing values:", df.isnull().sum().sum())
print("Duplicates:", df.duplicated().sum())

if df.duplicated().sum() > 0:
    df = df.drop_duplicates().reset_index(drop=True)
    print("✅ Duplicates removed. New shape:", df.shape)

# ----------------------------
# 4. Analysis Questions
# ----------------------------
print("\n📊 Analysis:")

# Q1 Average final grade
avg_g3 = df["G3"].mean()
print(f"1) Average final grade (G3): {avg_g3:.2f}")

# Q2 Students scored above 15
above_15 = (df["G3"] > 15).sum()
print(f"2) Students scoring above 15: {above_15} out of {len(df)}")

# Q3 Correlation between study time and G3
spearman_corr = df["studytime"].corr(df["G3"], method="spearman")
pearson_corr = df["studytime"].corr(df["G3"], method="pearson")
print(f"3) Correlation studytime vs G3 → Spearman: {spearman_corr:.3f}, Pearson: {pearson_corr:.3f}")

# Q4 Gender comparison
gender_avg = df.groupby("sex")["G3"].mean().rename({"F": "Female", "M": "Male"})
print("4) Average grade by gender:\n", gender_avg, "\n")

# ----------------------------
# 5. Visualizations
# ----------------------------

# Histogram of grades
plt.figure()
df["G3"].plot(kind="hist", bins=21, edgecolor="black")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Count")
plt.title("Distribution of Final Grades")
plt.savefig(os.path.join(OUTPUTS_DIR, "hist_grades.png"), dpi=150)
plt.close()

# Scatterplot: studytime vs grades
plt.figure()
jitter = np.random.uniform(-0.1, 0.1, size=len(df))
plt.scatter(df["studytime"] + jitter, df["G3"], alpha=0.6)
plt.xticks([1,2,3,4], ["<2h","2-5h","5-10h",">10h"])
plt.xlabel("Study Time Category")
plt.ylabel("Final Grade (G3)")
plt.title("Study Time vs Final Grade")
plt.savefig(os.path.join(OUTPUTS_DIR, "scatter_studytime.png"), dpi=150)
plt.close()

# Bar chart: male vs female average score
plt.figure()
avg_by_sex = df.groupby("sex")["G3"].mean().rename({"F": "Female", "M": "Male"})
avg_by_sex.plot(kind="bar", color=["skyblue", "orange"])
plt.xlabel("Gender")
plt.ylabel("Average Final Grade")
plt.title("Average G3 by Gender")
plt.savefig(os.path.join(OUTPUTS_DIR, "bar_gender.png"), dpi=150)
plt.close()

print("📈 Visualizations saved in 'outputs/' folder")

# ----------------------------
# 6. Save outputs
# ----------------------------
# Cleaned CSV
cleaned_csv = os.path.join(OUTPUTS_DIR, "student-mat_clean.csv")
df.to_csv(cleaned_csv, index=False)

# Excel export
cleaned_xlsx = os.path.join(OUTPUTS_DIR, "student-mat.xlsx")
df.to_excel(cleaned_xlsx, index=False)

# Summary text
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

print("✅ Outputs saved: cleaned CSV, Excel, summary.txt, and charts in outputs/")

