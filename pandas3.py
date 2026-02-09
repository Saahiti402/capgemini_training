import pandas as pd
df = pd.DataFrame([['a', 'b'], ['c', 'd']], index = ['row1', 'row2'], columns = ['col1', 'col2'])
print(df.to_json(orient = 'split'))
print(df.to_json(orient='index'))