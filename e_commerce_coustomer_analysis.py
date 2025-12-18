import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Generate synthetic dataset (500+ rows)
np.random.seed(42)
num_records = 500

data = {
    "TransactionID": np.arange(1, num_records + 1),
    "Amount (USD)": np.round(np.random.exponential(scale=120, size=num_records), 2),
    "CustomerAge": np.random.randint(18, 71, num_records),
    "Region": np.random.choice(["North", "South", "East", "West"], num_records),
    "TimeSpentMinutes": np.random.randint(1, 61, num_records)
}

df = pd.DataFrame(data)

# Save as Excel
excel_path = "Transaction_Data.xlsx"
df.to_excel(excel_path, index=False)

# 2. Descriptive statistics for Amount (USD)
stats = df["Amount (USD)"].describe()
print("Summary Statistics for Amount (USD):")
print(stats)

# 3. Bar chart - Transaction count per Region
plt.hist(df['PurchaseAmount'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Purchase Amount')
plt.xlabel('Purchase Amount')
plt.ylabel('Frequency')
plt.show()

df['ProductCategory'].value_counts().plot(kind='bar', color='lightgreen')
plt.title('Product Category Counts')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.show()

# 4. Average transaction amount per Region
avg_amount_region = df.groupby("Region")["Amount (USD)"].mean()
print("\nAverage Transaction Amount per Region:")
print(avg_amount_region)

sns.boxplot(x='ProductCategory', y='PurchaseAmount', data=df)
plt.title('Purchase Amount by Product Category')
plt.show()


# 6. Correlation between Time Spent and Amount
correlation = df["TimeSpentMinutes"].corr(df["Amount (USD)"])
print("\nCorrelation between Time Spent and Amount (USD):", correlation)

