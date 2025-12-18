import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
plt.figure(figsize=(6,4))
df["Region"].value_counts().plot(kind="bar")
plt.title("Transaction Count per Region")
plt.xlabel("Region")
plt.ylabel("Number of Transactions")
plt.show()

# 4. Average transaction amount per Region
avg_amount_region = df.groupby("Region")["Amount (USD)"].mean()
print("\nAverage Transaction Amount per Region:")
print(avg_amount_region)

# 5. Scatter plot - Time Spent vs Amount (USD)
plt.figure(figsize=(6,4))
plt.scatter(df["TimeSpentMinutes"], df["Amount (USD)"])
plt.title("Time Spent vs Transaction Amount")
plt.xlabel("Time Spent (Minutes)")
plt.ylabel("Amount (USD)")
plt.show()

# 6. Correlation between Time Spent and Amount
correlation = df["TimeSpentMinutes"].corr(df["Amount (USD)"])
print("\nCorrelation between Time Spent and Amount (USD):", correlation)

