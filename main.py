import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"F:\New folder (2)\csv\book.csv")

# Bar Chart 1: Total Sales by Product
product_sales = df.groupby('Product')['Total_Sales'].sum()
plt.figure(figsize=(8,6))
plt.bar(product_sales.index, product_sales.values, color='skyblue')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar Chart 2: Total Sales by Region
region_sales = df.groupby('Region')['Total_Sales'].sum()
plt.figure(figsize=(8,6))
plt.bar(region_sales.index, region_sales.values, color='lightgreen')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar Chart 3: Number of Purchases by Customer
customer_counts = df['Customer_ID'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.bar(customer_counts.index.astype(str), customer_counts.values, color='salmon')
plt.title("Top 10 Customers by Purchase Count")
plt.xlabel("Customer ID")
plt.ylabel("Number of Purchases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

