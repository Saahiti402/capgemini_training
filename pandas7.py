import pandas as pd
import numpy as np
# data = np.array(['s', 'a', 'a', 'h', 'i', 't', 'i', 'k', 's'])
# ser = pd.Series(data)
# print(ser[:5])

data = np.array(['s', 'a', 'a', 'h', 'i', 't', 'i', 'k', 's'])
ser = pd.Series(data, index=[10, 11, 12, 13, 14, 15, 16, 17, 18])
print(ser[16])