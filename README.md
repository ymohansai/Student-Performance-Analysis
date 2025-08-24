# 🎓 Student Performance Analysis
**Data Science Internship – Task 1 (Maincrafts)**  

This project analyzes the **UCI Student Performance dataset** using Python (pandas, numpy, matplotlib, seaborn).  
It demonstrates the **data science workflow**:  
**Load → Clean → Analyze → Visualize → Conclude**

---

## 📊 Dataset
- Source: [UCI Machine Learning Repository – Student Performance Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip)  
- File used: `student-mat.csv` (Math course)  

---

## 🛠 Tools & Libraries
- Python 3.10+  
- pandas, numpy  
- matplotlib, seaborn  
- scipy (for correlation)  
- openpyxl (for Excel export)  

---

## 📂 Project Structure
```
Student-Performance-Analysis/
│── data/
│   └── student-mat.csv        # dataset (place here)
│── outputs/                   # generated results
│── main.py                    # main project script
│── requirements.txt           # dependencies
│── README.md
```

---

## 🚀 How to Run

1. **Clone repo**
   ```bash
   git clone https://github.com/ymohansai/Student-Performance-Analysis.git
   cd Student-Performance-Analysis
   ```

2. **Create venv & install requirements**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```

3. **Run script**
   ```bash
   python main.py
   ```

4. **Outputs generated in `outputs/`**:
   - 📊 Histogram of grades (`hist_grades.png`)
   - 📈 Study time vs grades scatterplot (`scatter_studytime.png`)
   - 🟦 Gender-wise bar chart (`bar_gender.png`)
   - 📝 Cleaned dataset (CSV + Excel)
   - 📄 Text summary (`summary.txt`)

---

## 📌 Analysis Performed
1. Average final grade (G3)  
2. Students scoring above 15  
3. Correlation: study time vs performance (Pearson & Spearman)  
4. Gender comparison (male vs female average grades)  

---

## 📷 Example Output
(Outputs will appear in `outputs/` after running the script)

---

## 📜 License
MIT License  
You are free to use and modify this project for learning purposes.
