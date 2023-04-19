import psycopg2
import json
import logging

## a function that connects to a postgres database hosted in azure and creates a table if not exists

def create_DB():

    with open('config.json') as f:
        config = json.load(f)

    try:
        conn = psycopg2.connect(
            dbname=config['<database-name>'],
            user=config['<admin-username>'],
            host=config['<server-name>'],
            password=config['<admin-password>']
        )
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS feedback (userid varchar(255), sessionid varchar(255), text varchar(255));")
        conn.commit()
        conn.close()
        logging.info("Table created successfully in PostgreSQL ")
    except Exception as e:
        logging.info("Error while connecting to PostgreSQL", e)
        print(e)