import pandas as pd

def transform(data):
    df = pd.json_normalize(data)
    df = df[['name', 'main.temp', 'main.humidity', 'weather']]
    df['weather'] = df['weather'].apply(lambda x: x[0]['description'])
    return df
