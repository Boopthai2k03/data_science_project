Import numpy as np
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
    "PurchaseAmount": np.round(np.random.exponential(scale=120, size=num_records), 2),
    "ProductCategory": np.random.choice(
        ["Electronics", "Clothing", "Furniture", "Toys"], num_records
    ),
    "Month": np.random.choice(
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], num_records
    )
})

# Save to CSV (Task 1)
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
# 3. Descriptive Statistics (Overall)
# ---------------------------
print("\nOverall Descriptive Statistics:")
print(df[["Age", "PurchaseAmount"]].describe())

# ---------------------------
# 4. Segmented Descriptive Statistics (Required Fix)
# ---------------------------
segmented_stats = df.groupby("ProductCategory")["PurchaseAmount"].agg(
    Mean="mean",
    Median="median",
    StdDev="std"
)

print("\nSegmented Descriptive Statistics by Product Category:")
print(segmented_stats)

# ---------------------------
# 5. Aggregation
# ---------------------------
sales_by_category = df.groupby("ProductCategory")["PurchaseAmount"].sum()
print("\nTotal Spending across Product Categories:")
print(sales_by_category)

# ---------------------------
# 6. Visualizations
# ---------------------------

# Histogram
plt.figure()
plt.hist(df["PurchaseAmount"], bins=10, edgecolor="black")
plt.title("Distribution of Purchase Amounts")
plt.xlabel("Purchase Amount")
plt.ylabel("Frequency")
plt.show()

# Bar Chart: Total Spending
plt.figure()
sales_by_category.plot(kind="bar")
plt.title("Total Spending across Product Categories")
plt.xlabel("Product Category")
plt.ylabel("Total Spending")
plt.show()
