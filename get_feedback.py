import psycopg2
import json


def get_feedback(userid):

    with open('config.json') as f:
        config = json.load(f)

    conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'".format(
        config['<database-name>'], config['<admin-username>'], config['<server-name>'], config['<admin-password>']))
    cur = conn.cursor()
    cur.execute("SELECT * FROM feedback WHERE userid = '{}'".format(userid))
    rows = cur.fetchall()
    data = []
    for row in rows:
        data.append({
            "userid": row[0],
            "sessionid": row[1],
            "feedback": row[2]
        })
    conn.close()
    return data
