import psycopg2
import json

def update_feedback(userid, sessionid, feedback):
    with open('config.json') as f:
        config = json.load(f)

    conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'".format(config['<database-name>'], config['<admin-username>'], config['<server-name>'], config['<admin-password>']))
    cur = conn.cursor()
    cur.execute("UPDATE feedback SET text = %s WHERE userid = %s AND sessionid = %s", (feedback, userid, sessionid))
    conn.commit()
    conn.close()
    return "Feedback updated successfully"