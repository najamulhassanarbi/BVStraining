"""
File: clean_data.py

Description:
    This script cleans and transforms product data from a JSON file. It:

    1. Loads the data into a pandas DataFrame.
    2. Cleans the 'price' column by removing currency symbols and converting it to float.
    3. Extracts the correct brand name from the 'brand' column.
    4. Normalizes the 'category' column by trimming and converting it to uppercase.
    5. Saves the cleaned data to "cleaned_data.json" and "cleaned_products.json".
"""

import pandas as pd

df = pd.read_json("/content/computer_zone_with_category.json")
df['price'] = df['price'].str.replace('Rs.', '').str.replace(',', '').astype(float)
df['brand'] = df['brand'].apply(lambda x: x[1] if len(x) > 1 else None)
df['category'] = df['category'].apply(lambda x: x.lstrip('/').split('-')[0].strip().upper())

df.to_json("cleaned_data.json", index=False)
df.to_json('cleaned_products.json', orient='records', lines=False)
