import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 1. Generate synthetic dataset
# ---------------------------
np.random.seed(42)
num_records = 500

df = pd.DataFrame({
    "CustomerID": np.arange(1, num_records + 1),
    "Age": np.random.randint(18, 70, num_records),
    "TransactionAmount": np.round(np.random.exponential(scale=120, size=num_records), 2),
    "ProductCategory": np.random.choice(
        ["Electronics", "Clothing", "Furniture", "Toys"], num_records
    )
})

# Save to CSV (Task 1 requirement)
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

# ---------------------------
# 4. Aggregation
# ---------------------------
sales_by_category = df.groupby("ProductCategory")["TransactionAmount"].sum()
print("\nTotal Spending across Product Categories:")
print(sales_by_category)

# ---------------------------
# 5. Visualizations
# ---------------------------

# Histogram
plt.figure()
plt.hist(df["TransactionAmount"], bins=10, edgecolor="black")
plt.title("Distribution of Transaction Amounts")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.show()

# Correct bar chart: Total Spending (SUM)
plt.figure()
sales_by_category.plot(kind="bar")
plt.title("Total Spending across Product Categories")
plt.xlabel("Product Category")
plt.ylabel("Total Spending")
plt.show()
