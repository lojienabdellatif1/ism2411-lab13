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

print("Unique regions:")
print(df['region'].unique())

print("Region counts:")
print(df['region'].value_counts())

print("Region counts (including nulls):")
print(df['region'].value_counts(dropna=False))

print("---exercise 7: select columns---")
subset = df[['region', 'product', 'revenue']]

print("Subset shape:", subset.shape)
print(subset.head())

print("---exercise 8: save---")

df.to_csv('data/explored.csv', index=False)
print("\nSaved to data/explored.csv")

#self reflection
#1: the boolean filter helped me to filter the data based on specific conditions, allowing me to focus on relevant subsets of the dataset.
#2: the diffrence between df["revenue"] and df[["revenue"]] is that the former returns a Series object, while the latter returns a DataFrame object. The double brackets are used to select multiple columns or to ensure the result is a DataFrame. it matters depending on what you want to use the data for
#3: if i had to explain to a colleague why i rather use pandas over excel, I would tell them that it is less tedious and less prone to errors. i think that most people hate excel because of these two things, and learning pandas can help eleviate these issues. pandas allows for more efficient data manipulation, analysis, and visualization, especially with larger datasets. It also provides a wide range of functions and methods that can automate repetitive tasks, making it easier to work with data programmatically.