from extract import extract
from transform import transform
from load import load

API_KEY = 'your_api_key_here'
CITY = 'London'

data = extract(API_KEY, CITY)
df = transform(data)
load(df)
print('ETL process completed successfully.')
