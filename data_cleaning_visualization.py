# Data Cleaning & Visualization Project
# Student Performance Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load raw data
df = pd.read_csv("raw_student_performance.csv")

# Inspect data
print(df.head())
print(df.info())
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates().reset_index(drop=True)

numeric_cols = [
    "Study_Hours_Per_Day","Attendance_Percent","Assignment_Score",
    "Sleep_Hours","Math_Score","Programming_Score","Communication_Score"
]

# Fill missing numeric values using median
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())

# Detect and treat outliers using IQR clipping
for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    df[col] = df[col].clip(lower, upper)

# Create average score and performance category
df["Average_Score"] = df[["Math_Score","Programming_Score","Communication_Score"]].mean(axis=1)

df["Performance_Level"] = pd.cut(
    df["Average_Score"],
    bins=[-np.inf, 50, 70, 85, np.inf],
    labels=["Needs Improvement","Average","Good","Excellent"]
)

# Save cleaned dataset
df.to_csv("cleaned_student_performance.csv", index=False)

# Visualization 1: subject averages
df[["Math_Score","Programming_Score","Communication_Score"]].mean().plot(kind="bar")
plt.title("Average Score by Subject")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()

# Visualization 2: department performance
df.groupby("Department")["Average_Score"].mean().sort_values(ascending=False).plot(kind="bar")
plt.title("Average Performance by Department")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()

# Visualization 3: study hours vs score
plt.scatter(df["Study_Hours_Per_Day"], df["Average_Score"], alpha=0.7)
plt.xlabel("Study Hours per Day")
plt.ylabel("Average Score")
plt.title("Study Hours vs Average Score")
plt.tight_layout()
plt.show()

# Visualization 4: attendance distribution
plt.hist(df["Attendance_Percent"], bins=10)
plt.xlabel("Attendance (%)")
plt.ylabel("Number of Students")
plt.title("Distribution of Attendance")
plt.tight_layout()
plt.show()

# Visualization 5: performance levels
df["Performance_Level"].value_counts().reindex(
    ["Needs Improvement","Average","Good","Excellent"], fill_value=0
).plot(kind="bar")
plt.title("Student Performance Levels")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

print("\nKey Findings:")
print("Average score:", round(df["Average_Score"].mean(), 2))
print("Highest-performing department:", df.groupby("Department")["Average_Score"].mean().idxmax())
print("Most common performance level:", df["Performance_Level"].value_counts().idxmax())
print("Correlation between study hours and average score:",
      round(df["Study_Hours_Per_Day"].corr(df["Average_Score"]), 2))
