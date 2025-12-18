import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 1. Generate Synthetic Dataset
# ---------------------------
np.random.seed(42)
num_records = 500

df = pd.DataFrame({
    "CustomerID": np.arange(1, num_records + 1),
    "Age": np.random.randint(18, 70, num_records),
    "TransactionAmount": np.round(
        np.random.exponential(scale=120, size=num_records), 2
    ),
    "ProductCategory": np.random.choice(
        ["Electronics", "Clothing", "Furniture", "Toys"], num_records
    )
})

# Generate Transaction Date spanning one year
df["TransactionDate"] = pd.to_datetime("2024-01-01") + pd.to_timedelta(
    np.random.randint(0, 365, num_records), unit="D"
)

# Save dataset
df.to_csv("customer_transactions.csv", index=False)

# ---------------------------
# 2. Initial Data Inspection
# ---------------------------
print("Dataset Shape:")
print(df.shape)

print("\nDataset Info:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

# ---------------------------
# 3. Descriptive Statistics
# ---------------------------
print("\nDescriptive Statistics:")
print(df[["Age", "TransactionAmount"]].describe())

# Explicit IQR Calculation
Q1 = df["TransactionAmount"].quantile(0.25)
Q3 = df["TransactionAmount"].quantile(0.75)
IQR = Q3 - Q1

print("\nInterquartile Range (IQR):", IQR)

# ---------------------------
# 4. Visualization
# ---------------------------

# Histogram
plt.figure()
plt.hist(df["TransactionAmount"], bins=10, edgecolor="black")
plt.title("Distribution of Transaction Amounts")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.show()

# Bar Chart: Average Transaction Amount per Category
avg_by_category = df.groupby("ProductCategory")["TransactionAmount"].mean()

plt.figure()
avg_by_category.plot(kind="bar")
plt.title("Average Transaction Amount per Product Category")
plt.xlabel("Product Category")
plt.ylabel("Average Transaction Amount")
plt.show()
