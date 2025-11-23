import psycopg2

def load(df):
    conn = psycopg2.connect(dbname='weather_db', user='etl_user', password='etl_pass', host='localhost')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS weather (city TEXT, temp FLOAT, humidity INT, description TEXT)''')
    for _, row in df.iterrows():
        cur.execute('INSERT INTO weather VALUES (%s, %s, %s, %s)', (row['name'], row['main.temp'], row['main.humidity'], row['weather']))
    conn.commit()
    cur.close()
    conn.close()
