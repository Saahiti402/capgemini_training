import pandas as pd
import requests
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
data = pd.json_normalize(response.json())
print(data.head())
