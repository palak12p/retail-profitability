import pandas as pd
import numpy as np
import random

# Define mock variables
cities = ["Indore", "Bhopal", "Raipur", "Nagpur", "Lucknow", "Varanasi", "Jabalpur", "Udaipur", "Jodhpur", "Ranchi"]
stores = [f"Store_{i+1}" for i in range(25)]
products = [f"Product_{i+1}" for i in range(50)]
categories = ['Grocery', 'Snacks', 'Beverages', 'Personal Care', 'Stationery']

# Generate synthetic data
data = []
for day in pd.date_range(start="2024-01-01", end="2024-03-31"):
    for store in stores:
        for _ in range(np.random.randint(5, 15)):  # transactions per store/day
            product = random.choice(products)
            category = random.choice(categories)
            price = np.round(np.random.uniform(20, 500), 2)
            quantity = np.random.randint(1, 5)
            cost = price * np.random.uniform(0.6, 0.9)
            city = random.choice(cities)
            data.append([
                day, store, city, product, category, price, quantity,
                np.round(price * quantity, 2), np.round(cost * quantity, 2)
            ])

# Create a DataFrame
df = pd.DataFrame(data, columns=[
    'Date', 'Store', 'City', 'Product', 'Category',
    'Unit_Price', 'Quantity', 'Revenue', 'Cost'
])

# Save to CSV
df.to_csv('data/retail_sales_data.csv', index=False)
print("✅ retail_sales_data.csv generated successfully.")
