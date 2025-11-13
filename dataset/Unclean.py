import pandas as pd
#import numpy as np
data = {
    'Name': ['sanket', 'Mayur', 'sherya', 'Chitu', 'Bindi', None],
    'Math_Score': [85, None, 78, 0, 92, 88],
    'Science_Score': [90, 75, None, 80, None, 70],
    'Computer':['C','java',None,'Python',None,'c++']
}

DB = pd.DataFrame(data)

print(DB)
print("\n")

df_any_removed = DB.drop()
print(df_any_removed)
print("\n")

df_any_removed=DB.index()
print(df_any_removed)
print("\n")

Avg=DB['Math_Score'].mean()
DB['Math_Score'].fillna(Avg,inplace=True)
print(DB)
