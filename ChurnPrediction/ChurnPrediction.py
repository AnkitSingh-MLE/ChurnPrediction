import pandas as pd  

# Load dataset from the given path
df = pd.read_csv(r"C:\Data_Science_Prep\Kaggle\Dataset\ChurnPrediction\WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Display first few rows
print(df.head())

# Check dataset shape (rows, columns)
print(f"Dataset Shape: {df.shape}")

# Check column data types and missing values
print(df.info())

# Summary statistics for numerical columns
print(df.describe())

# Count missing values in each column
print(df.isnull().sum())

# Check unique values in each column
print(df.nunique())

#Check Churn Distribution (Target Variable)
import matplotlib.pyplot as plt  
import seaborn as sns  

# Countplot for churn column
plt.figure(figsize=(6,4))
sns.countplot(x=df["Churn"], palette="pastel")
plt.title("Churn Distribution")
plt.show()

# Percentage of Churned vs. Retained Customers
churn_rate = df["Churn"].value_counts(normalize=True) * 100
print(churn_rate)

