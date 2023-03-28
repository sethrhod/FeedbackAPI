import psycopg2

def update_feedback(uuid, sessionid, feedback):
    conn = psycopg2.connect("dbname=test user=postgres")
    cur = conn.cursor()
    cur.execute("UPDATE feedback SET feedback = %s WHERE sessionid = %s AND uuid = %s", (feedback, sessionid, uuid))
    conn.commit()
    conn.close()