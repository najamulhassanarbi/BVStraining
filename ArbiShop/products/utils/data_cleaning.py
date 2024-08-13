import pandas as pd
import json


df = pd.read_json("/content/computer_zone_with_category.json")
df['price'] = df['price'].str.replace('Rs.', '').str.replace(',', '').astype(float)
df['brand'] = df['brand'].apply(lambda x: x[1] if len(x) > 1 else None)
df['category'] = df['category'].apply(lambda x: x.lstrip('/').split('-')[0].strip().upper())

df.to_json("cleaned_data.json", index=False)
df.to_json('cleaned_products.json', orient='records', lines=False)