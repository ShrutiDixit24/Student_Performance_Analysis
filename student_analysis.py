import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv("StudentsPerformance.csv")

print("First 5 rows of dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
df["Total_Score"] = df[["math score", "reading score", "writing score"]].sum(axis=1)
df["Average_Score"] = df["Total_Score"] / 3
def assign_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

df["Grade"] = df["Average_Score"].apply(assign_grade)
df["Status"] = np.where(df["Grade"] == "Fail", "Needs Improvement", "Pass")
gender_avg = df.groupby("gender")[["math score", "reading score", "writing score"]].mean()
print("\nGender-wise Average Scores:")
print(gender_avg)
test_prep_avg = df.groupby("test preparation course")["Average_Score"].mean()
print("\nTest Preparation vs Average Score:")
print(test_prep_avg)
parent_edu_avg = df.groupby("parental level of education")["Average_Score"].mean()
print("\nParental Education vs Average Score:")
print(parent_edu_avg)
lunch_avg = df.groupby("lunch")["Average_Score"].mean()
print("\nLunch Type vs Average Score:")
print(lunch_avg)
top_students = df.sort_values(by="Average_Score", ascending=False).head(5)
print("\nTop 5 Students:")
print(top_students)
weak_students = df[df["Average_Score"] < 50]
print("\nStudents Needing Improvement:")
print(weak_students)
print("\nOverall Statistics:")
print(df.describe())
df.to_csv("output/final_report.csv", index=False)
print("\nFinal report saved successfully!")
gender_avg = df.groupby("gender")["Average_Score"].mean()
test_prep_avg = df.groupby("test preparation course")["Average_Score"].mean()
subject_avg = df[["math score", "reading score", "writing score"]].mean()

# --------- DATA VISUALIZATION ---------
plt.figure(figsize=(14, 9))
plt.suptitle(
    "Student Performance Analysis Dashboard",
    fontsize=18,
    fontweight="bold"
)

# -------- Graph 1: Gender vs Average Score --------
plt.subplot(2, 2, 1)
ax1 = gender_avg.plot(kind="bar")
plt.title("Gender-wise Average Score", fontsize=12)
plt.xlabel("Gender")
plt.ylabel("Average Score")

for p in ax1.patches:
    ax1.annotate(
        f"{p.get_height():.1f}",
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha="center", va="bottom"
    )

# -------- Graph 2: Test Preparation Impact --------
plt.subplot(2, 2, 2)
ax2 = test_prep_avg.plot(kind="bar")
plt.title("Impact of Test Preparation", fontsize=12)
plt.xlabel("Test Preparation Course")
plt.ylabel("Average Score")

for p in ax2.patches:
    ax2.annotate(
        f"{p.get_height():.1f}",
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha="center", va="bottom"
    )

# -------- Graph 3: Subject-wise Performance --------
plt.subplot(2, 1, 2)
ax3 = subject_avg.plot(kind="bar")
plt.title("Subject-wise Average Scores", fontsize=12)
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

for p in ax3.patches:
    ax3.annotate(
        f"{p.get_height():.1f}",
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha="center", va="bottom"
    )

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("output/student_dashboard.png", dpi=300)

plt.show()
