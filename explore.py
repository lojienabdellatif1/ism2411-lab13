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

print("South rows:", len(south))
print(south.head())

print("---exercise 3: top 5 by revenue---")
top5 = df.sort_values('revenue', ascending=False).head(5)

print("\nTop 5 by revenue:")
print(top5)

print("---exercise 4: two condition filter---")
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print("Big South rows:", len(big_south))
print(big_south.head())

print("---exercise 5: a new column---")
df['per_unit'] = df['revenue'] / df['quantity']

print("\nWith per_unit column:")
print(df.head())
print("\nMean per-unit price:", df['per_unit'].mean())

print("---exercise 6:unique values---")
# Exercise 6: unique values
print("Unique regions:")
print(df['region'].unique())

print("Region counts:")
print(df['region'].value_counts())

print("Region counts (including nulls):")
print(df['region'].value_counts(dropna=False))