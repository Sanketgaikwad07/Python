import pandas as pd

data = {
    'Title': ['Book A', 'Book B', 'Book C'],
    'Author': ['Author X', 'Author Y', 'Author Z'],
    'Price': [250, 300, 150],
    'Year': [2020, 2021, 2019]
}

df = pd.DataFrame(data)
df.to_csv('book_dataset.csv', index=False)
print("✅ Sample CSV file created successfully!")
