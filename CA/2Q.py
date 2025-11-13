#NumPy

import numpy as np

def fill_nan_with_column_mean(arr):
   
    column_means = np.nanmean(arr, axis=0, keepdims=True)
    nan_mask = np.isnan(arr)

    arr[nan_mask] = np.tile(column_means, (arr.shape[0], 1))[nan_mask]
    
    return arr

data = np.array([[1.0, 2.0, np.nan],
                 [4.0, np.nan, 6.0],
                 [7.0, 8.0, 9.0],
                 [2 , 10.0, 11.0]])

print("Original array:")
print(data)

filled_data = fill_nan_with_column_mean(data.copy()) # Use .copy() to avoid modifying the original array

print("\nArray after filling NaN values:")
print(filled_data)
