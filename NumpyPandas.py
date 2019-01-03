import pandas as pd
import numpy as np

print('test for the np.all')

# data frame
A = pd.DataFrame([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [5, 8, 9, 11, 9]],
                 columns=['a', 'b', 'c', 'd', 'e'])

# conditions for each columns to drop the rows
c_rows = np.all([A['a'] > 3,
                 A['b'] < 9,
                 A['c'] < 10,
                 A['d'] < 10,
                 A['e'] > 8],
                axis=0)

print('Before')
print(A)
print('After')
print(A[c_rows])


print('\ntest for the np.any')

# conditions for each columns to drop the rows
c_rows = np.any([A['a'] > 3,
                 A['b'] < 9,
                 A['c'] < 10,
                 A['d'] < 10,
                 A['e'] > 8],
                axis=0)

print('Before')
print(A)
print('After')
print(A[c_rows])

