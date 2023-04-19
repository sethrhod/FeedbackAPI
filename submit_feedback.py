from user_Class import User
import psycopg2
import json

def submit_feedback(uuid, sessionid, feedback):

    with open('config.json') as f:
        config = json.load(f)

    conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'".format(config['<database-name>'], config['<admin-username>'], config['<server-name>'], config['<admin-password>']))    
    cur = conn.cursor()
    cur.execute("INSERT INTO feedback (userid, sessionid, text) VALUES (%s, %s, %s)", (uuid, sessionid, feedback))
    conn.commit()
    conn.close()
    return "Feedback submitted successfully"

