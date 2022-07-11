import pandas as pd
penguins = pd.read_csv('penguins_cleaned.csv')

# Ordinal feature encoding
df = penguins.copy()
target = 'species'
encode = ['sex', 'islands']