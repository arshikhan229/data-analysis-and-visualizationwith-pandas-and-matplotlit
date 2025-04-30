#📄 Data Analysis and Visualization – Code Summary

#✅ 1. Load & Inspect Data
import pandas as pd
import seaborn as sns

df = pd.read_csv("sales_data.csv")
print(df.head())
print(df.info())

#🧼 2. Clean the Data
df["Order Date"] = pd.to_datetime(df["Order Date"])
df.dropna(inplace=True)
df["Total"] = df["Quantity"] * df["Unit Price"]

#🔎 3. Explore the Data
print(df.describe())
print(df["Region"].value_counts())

#📊 4. Visualize with Matplotlib & Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Monthly trend
df.set_index("Order Date", inplace=True)
monthly = df["Total"].resample("M").sum()
monthly.plot(title="Monthly Sales Trend")
plt.show()

# Top products
top_products = df.groupby("Product")["Total"].sum().nlargest(5)
top_products.plot(kind="bar", title="Top 5 Products")
plt.show()

# Pie chart of regional sales
df.groupby("Region")["Total"].sum().plot(kind="pie", autopct='%1.1f%%')
plt.title("Revenue by Region")
plt.ylabel("")
plt.show()

#📑 5. Grouping and Aggregating
grouped = df.groupby(["Region", "Product"])["Total"].sum().reset_index()
print(grouped.sort_values(by="Total", ascending=False).head())

#📁 6. Export Results
df.to_csv("sales_cleaned.csv", index=False)
plt.savefig("monthly_sales_chart.png")

#📚 7. Real-World Project Patterns
# Filter, sort, top-N analysis
df[df["Region"] == "East"].sort_values("Total", ascending=False).head()

# Time-based trend
df["Month"] = df.index.to_period("M")
df.groupby("Month")["Total"].sum().plot(title="Monthly Revenue")
plt.grid(True)
plt.show()


