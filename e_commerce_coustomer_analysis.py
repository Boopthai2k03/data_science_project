import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# 1. Generate synthetic dataset
# ---------------------------
np.random.seed(42)
num_records = 500

df = pd.DataFrame({
    "Customer ID": np.arange(1, num_records + 1),
    "Transaction Amount": np.round(np.random.exponential(scale=120, size=num_records), 2),
    "Product Category": np.random.choice(
        ["Electronics", "Clothing", "Furniture", "Toys"], num_records
    ),
    "Purchase Date": pd.date_range(start="2025-01-01", periods=num_records, freq="D")
})

# ---------------------------
# 2. Descriptive statistics for Transaction Amount
# ---------------------------
transaction_stats = df["Transaction Amount"].describe()
print("Descriptive Statistics for Transaction Amount:")
print(transaction_stats)

# Add median, Q1, Q3 explicitly
print("\nAdditional Stats:")
print("Median:", df["Transaction Amount"].median())
print("Q1 (25%):", df["Transaction Amount"].quantile(0.25))
print("Q3 (75%):", df["Transaction Amount"].quantile(0.75))

# ---------------------------
# 3. Total sales per Product Category
# ---------------------------
sales_by_category = df.groupby("Product Category")["Transaction Amount"].sum()
print("\nTotal Sales Volume per Product Category:")
print(sales_by_category)

# ---------------------------
# 4. Visualizations
# ---------------------------

# Histogram of Transaction Amount
plt.figure()
plt.hist(df["Transaction Amount"], bins=10, edgecolor="black", color="skyblue")
plt.title("Histogram of Transaction Amount")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.show()

# Bar chart of Product Category counts
plt.figure()
df["Product Category"].value_counts().plot(kind="bar", color="lightgreen")
plt.title("Product Category Counts")
plt.xlabel("Product Category")
plt.ylabel("Count")
plt.show()

# Boxplot: Transaction Amount by Product Category
plt.figure()
sns.boxplot(x="Product Category", y="Transaction Amount", data=df)
plt.title("Transaction Amount by Product Category")
plt.show()
