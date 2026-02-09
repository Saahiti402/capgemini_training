import json
import requests
import pandas as pd
from pandas import json_normalize
# 
# with open('/content/raw_nyc_phil.json') as f:
#     d = json.load(f)
response = requests.get('https://jsonplaceholder.typicode.com/posts')    
nycphil = json_normalize(response.json())
print(nycphil.head(3))