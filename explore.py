import pandas as pd

df = pd.read_csv("data/retail_sales.csv")
print(df.head())

print("---exercise 1: load it---")
df = pd.read_csv("data/retail_sales.csv")

print("First 5 rows:")
print(df.head())
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)

print("---exercise 2: filter by region---")
south = df[df['region'] == 'South']

print("\nSouth rows:", len(south))
print(south.head())

print("---exercise 3: top 5 by revenue---")
top5 = df.sort_values('revenue', ascending=False).head(5)

print("\nTop 5 by revenue:")
print(top5)