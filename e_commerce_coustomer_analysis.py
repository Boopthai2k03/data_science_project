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
    "ProductCategory": np.random.choice(["Electronics", "Clothing", "Furniture", "Toys"], num_records),
    "TimeSpentMinutes": np.random.randint(1, 61, num_records),
    "IsReturned": np.random.choice([0, 1], num_records),  # 0 = not returned, 1 = returned
    "TransactionDate": pd.date_range(start='2025-01-01', periods=num_records, freq='D')
}

df = pd.DataFrame(data)

# Save as Excel
excel_path = "Transaction_Data_Corrected.xlsx"
df.to_excel(excel_path, index=False)

# 2. Descriptive statistics for PurchaseAmount
stats = df["PurchaseAmount"].describe()
print("Summary Statistics for PurchaseAmount:")
print(stats)

# 3a. Histogram of PurchaseAmount
plt.hist(df['PurchaseAmount'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Purchase Amount')
plt.xlabel('Purchase Amount')
plt.ylabel('Frequency')
plt.show()

# 3b. Bar chart of ProductCategory counts
df['ProductCategory'].value_counts().plot(kind='bar', color='lightgreen')
plt.title('Product Category Counts')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.show()

# 3c. Box plot comparing PurchaseAmount across ProductCategory
sns.boxplot(x='ProductCategory', y='PurchaseAmount', data=df)
plt.title('Purchase Amount by Product Category')
plt.show()

# 4. Frequency distribution of categorical variables
category_counts = df['ProductCategory'].value_counts()
print("\nFrequency Distribution of ProductCategory:")
print(category_counts)

