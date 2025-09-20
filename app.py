import pandas as pd

# 1.Load dataset
df = pd.read_csv("employees.csv")
print("Original Data:\n",df)

# 2.Check for missing values
print("\nMissing Values:\n",df.isnull().sum())

# 3.Fill missing Experince with averge
df["Experience"].fillna(df["Experience"].mean(),inplace=True)

# 4. Fill missing Salary with median
df["Salary"].fillna(df["Salary"].median(),inplace=True)

# 5. Department-wise employee count
dept_count = df["Department"].value_counts()
print("\nEmployees in each Department:\n",dept_count)

# 6. Average Salary by Department
avg_saraly = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:\n",avg_saraly)

# 7.Highest Paid Employee
highst_paid = df.loc[df["Salary"].idxmax()]
print("\nHighest Paid Employee:\n",highst_paid)

# 8. Save cleaned dataset
df.to_csv("cleaned_employees.csv",index=False)
print("\nCleaned data saved as 'cleaned_employees.csv'")