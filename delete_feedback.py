import psycopg2
import json


def delete_feedback(userid, sessionid, feedback):
    with open('config.json') as f:
      config = json.load(f)

    conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'".format(
        config['<database-name>'], config['<admin-username>'], config['<server-name>'], config['<admin-password>']))
    cur = conn.cursor()
    cur.execute("DELETE FROM feedback WHERE userid = %s AND sessionid = %s AND text = %s",
                (userid, sessionid, feedback))
    conn.commit()
    conn.close()
    return "Feedback deleted successfully"
