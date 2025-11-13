import pandas as pd
data = {
    'Title': ['joker', 'iron man', 'The Dark Knight', 'Avengers: Endgame', 'Joker'],
    'Year': [2010, 2014, 2008, 2019, 2019],
    'Genre': ['Sci-Fi', 'Sci-Fi', 'Action', 'Action', None], 
    'Rating': [8.8, 8.6, 9.0, 8.4, 8.5],
    'Duration': [2.34,1.45,2.00,1.55,2.33]
}

movies_df = pd.DataFrame(data)#create  obj
print(movies_df.duplicated)
data.update()
# seriee_df = pd.DataFrame(data.copy)
# print(seriee_df)

print("First 3 rows:")
print(movies_df.tail(3))
print("\n")

print("Second 2 row: ")
print(movies_df.head(2))
print("\n")

print("Thrid 3 row: ")
print(movies_df.dtypes)
print("\n")

print("4 row")
print(movies_df.isnull().sum())
print("\n")

print("5 row")
print(movies_df.describe)
#print
