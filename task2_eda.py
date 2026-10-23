
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
file_name = "ApexPlanet_DataAnalytics_Dataset.xlsx"
df = pd.read_excel(file_name)

# Create output folder
os.makedirs("outputs", exist_ok=True)

# 1. Basic information
print("\n===== DATASET INFORMATION =====")
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

# 2. Missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# 3. Duplicate checks
print("\nExact duplicate rows:", df.duplicated().sum())
print("Repeated Order IDs:", df["Order_ID"].duplicated().sum())

# 4. Descriptive statistics
print("\n===== NUMERICAL SUMMARY =====")
print(df.describe())

print("\n===== CATEGORICAL SUMMARY =====")
for col in ["Gender", "City", "Product", "Category"]:
    print(f"\n{col} frequency:")
    print(df[col].value_counts(dropna=False))

# 5. Save summary files
df.describe(include="all").transpose().to_csv(
    "outputs/descriptive_statistics.csv"
)

df.isnull().sum().rename("Missing_Count").to_csv(
    "outputs/missing_values.csv"
)

# 6. Prepare dates and monthly sales
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"], errors="coerce"
)

monthly_sales = (
    df.dropna(subset=["Order_Date"])
    .set_index("Order_Date")["Total_Sales"]
    .resample("MS")
    .sum()
)

plt.figure(figsize=(10, 5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/monthly_sales.png")
plt.close()

# 7. Sales by category
category_sales = df.groupby(
    "Category"
)["Total_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 5))
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/category_sales.png")
plt.close()

# 8. Age distribution
plt.figure(figsize=(8, 5))
df["Age"].dropna().plot(kind="hist", bins=10)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig("outputs/age_distribution.png")
plt.close()

# 9. Correlation heatmap
numeric_df = df[
    ["Age", "Quantity", "Unit_Price", "Total_Sales"]
]

plt.figure(figsize=(8, 6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png")
plt.close()

# 10. Save category summary
category_sales.to_csv("outputs/category_sales.csv")

print("\nEDA completed successfully!")
print("Check the outputs folder for CSV reports and charts.")
