import psycopg2
import json

## a function that connects to a postgres database hosted in azure and creates a table if not exists

def create_table():

    with open('config.json') as f:
        config = json.load(f)

    try:
        conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'".format(config['<database-name>'], config['<admin-username>'], config['<server-name>'], config['<admin-password>']))
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS feedback (userid varchar(255), sessionid varchar(255), feedback varchar(255));")
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)