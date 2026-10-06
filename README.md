# Data Cleaning & Visualization Project

## 📌 Project Overview

This project demonstrates a complete data-cleaning and visualization workflow using Python and a student performance dataset.

The workflow takes raw data, cleans and validates it, performs basic analysis, and creates visualizations to identify patterns and relationships in student performance.

> **Dataset note:** The dataset used in this project is synthetic/sample data created for educational purposes. It does not contain real student personal or academic records.

## 🎯 Objectives

- Handle missing values
- Detect and remove duplicate records
- Identify and treat outliers using the IQR method
- Check and correct data types
- Calculate average student scores
- Classify student performance
- Analyze performance by department
- Perform subject-wise analysis
- Study the relationship between study hours and performance
- Create clear and professional visualizations

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook / VS Code

## 📂 Project Structure

```text
data-cleaning-visualization/
│
├── README.md
├── .gitignore
├── data/
│   ├── raw_student_performance.csv
│   └── cleaned_student_performance.csv
│
├── src/
│   └── data_cleaning_visualization.py
│
├── visualizations/
│   ├── 01_average_subject_scores.png
│   ├── 02_department_performance.png
│   ├── 03_study_hours_vs_score.png
│   ├── 04_attendance_distribution.png
│   ├── 05_performance_levels.png
│   └── 06_correlation_matrix.png
│
└── report/
    └── Data_Cleaning_Visualization_Project_Report.docx
```

## 🧹 Data Cleaning Process

The project demonstrates:

1. Missing-value detection and handling
2. Duplicate-record detection and removal
3. Outlier detection using the Interquartile Range (IQR) method
4. Data-type checking
5. Validation of cleaned data

The original dataset contains 123 records, including intentionally introduced missing values, duplicate records, and unrealistic/outlier values. After cleaning, the dataset contains 120 valid student records.

## 📊 Analysis Performed

The project calculates and analyzes:

- Average subject scores
- Overall student performance
- Department-wise performance
- Subject-wise performance
- Attendance patterns
- Study hours versus average score
- Correlations between numerical variables

The cleaned dataset shows an approximately **0.64 correlation between study hours and average score**, indicating a moderate positive relationship in this sample.

## 📈 Visualizations

The project includes six visualizations:

- Average score by subject
- Department performance
- Study hours vs. average score
- Attendance distribution
- Performance-level distribution
- Correlation matrix

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd data-cleaning-visualization
```

### 2. Install the required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### 3. Run the Python script

```bash
python src/data_cleaning_visualization.py
```

## 💡 Key Learning Outcomes

This project provides practical experience with:

- Data preprocessing
- Exploratory data analysis
- Pandas DataFrames
- Missing-data handling
- Duplicate detection
- Outlier treatment
- Statistical calculations
- Data visualization
- Interpreting correlations
- Organizing a data science project for GitHub

## 📄 Documentation

The detailed project report is available in the `report/` folder.

## 👩‍💻 Author

**Srushti Patil**

B.Tech Computer Science Engineering

---

⭐ If you find this project useful, consider giving the repository a star!
