import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Generate synthetic dataset (500 rows)
np.random.seed(42)
num_records = 500

data = {
    "TransactionID": np.arange(1, num_records + 1),
    "PurchaseAmount": np.round(np.random.exponential(scale=120, size=num_records), 2),
    "CustomerAge": np.random.randint(18, 71, num_records),
    "ProductCategory": np.random.choice(
        ["Electronics", "Clothing", "Furniture", "Toys"], num_records
    ),
    "TimeSpentMinutes": np.random.randint(1, 61, num_records),
    "IsReturned": np.random.choice([0, 1], num_records),
    "TransactionDate": pd.date_range(start="2025-01-01", periods=num_records, freq="D")
}

df = pd.DataFrame(data)

# --------------------------------------------------
# 2. Descriptive statistics for ALL numerical columns
# --------------------------------------------------

numerical_columns = df.select_dtypes(include=["int64", "float64"])

stats_all = numerical_columns.agg(
    ["mean", "median", "std", "min", "max", "count"]
).T

# Add quartiles separately
stats_all["Q1 (25%)"] = numerical_columns.quantile(0.25)
stats_all["Q3 (75%)"] = numerical_columns.quantile(0.75)

print("\nDescriptive Statistics for ALL Numerical Columns:")
print(stats_all)

# --------------------------------------------------
# 3. Frequency distribution for categorical variables
# --------------------------------------------------

print("\nFrequency Distribution of ProductCategory:")
print(df["ProductCategory"].value_counts())

print("\nFrequency Distribution of IsReturned:")
print(df["IsReturned"].value_counts())

# --------------------------------------------------
# 4. Visualizations
# --------------------------------------------------

# Histogram of PurchaseAmount
plt.hist(df["PurchaseAmount"], bins=10, edgecolor="black")
plt.title("Histogram of Purchase Amount")
plt.xlabel("Purchase Amount")
plt.ylabel("Frequency")
plt.show()

# Bar chart of ProductCategory
df["ProductCategory"].value_counts().plot(kind="bar")
plt.title("Product Category Counts")
plt.xlabel("Product Category")
plt.ylabel("Count")
plt.show()

# Boxplot: PurchaseAmount vs ProductCategory
sns.boxplot(x="ProductCategory", y="PurchaseAmount",
 data=df)
plt.title("Purchase Amount by Product Category")
plt.show()

