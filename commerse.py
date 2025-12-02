import numpy as np
import pandas as pd
from openpyxl import Workbook
import matplotlib.pyplot as plt

# 1. Generate synthetic dataset (500+ rows)
np.random.seed(42)
num_records = 500

data = {
    "CustomerID": np.arange(1, num_records + 1),
    "Age": np.random.randint(18, 71, num_records),
    "TimeSpentMinutes": np.random.randint(1, 61, num_records),
    "PurchaseAmountUSD": np.round(np.random.uniform(10, 500, num_records), 2)
}

df = pd.DataFrame(data)

# Save as Excel
excel_path = "Ecommerce_Customers.xlsx"
df.to_excel(excel_path, index=False)

# 2. Descriptive statistics
stats = df[["Age", "TimeSpentMinutes", "PurchaseAmountUSD"]].describe()
print(stats)

# 3. Histogram - PurchaseAmountUSD
plt.figure(figsize=(6,4))
plt.hist(df["PurchaseAmountUSD"])
plt.title("Distribution of Purchase Amount (USD)")
plt.xlabel("Purchase Amount (USD)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - TimeSpent vs PurchaseAmount
plt.figure(figsize=(6,4))
plt.scatter(df["TimeSpentMinutes"], df["PurchaseAmountUSD"])
plt.title("Time Spent vs Purchase Amount")
plt.xlabel("Time Spent (Minutes)")
plt.ylabel("Purchase Amount (USD)")
plt.show()

# 5. Correlation
correlation = df["TimeSpentMinutes"].corr(df["PurchaseAmountUSD"])
print("Correlation:", correlation)
