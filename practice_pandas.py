import pandas as pd

df = pd.DataFrame({
    'product': ['A', 'B', 'C', 'D', 'E'],
    'price': [100, None, 300, None, 500],
    'category': ['Electronics', None, 'Clothing', 'Electronics', None],
    'rating': [4.5, 3.0, None, 4.0, None]
})

'''
Find how many nulls are in each column
Fill price nulls with mean of price
Fill category nulls with 'Unknown'
Fill rating nulls with median of rating
Verify no nulls remain using isnull().sum()

go.
'''
print(df.isnull().sum())
df['price'] = df['price'].fillna(df['price'].mean())
df['category'] = df['category'].fillna('Unknown')
df['rating'] = df['rating'].fillna(df['rating'].median())


print(df.isnull().sum())

