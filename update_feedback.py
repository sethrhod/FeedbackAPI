import psycopg2

def update_feedback(userid, sessionid, feedback):
    conn = psycopg2.connect("dbname=test user=postgres")
    cur = conn.cursor()
    cur.execute("UPDATE feedback SET feedback = %s WHERE userid = %s AND sessionid = %s", (feedback, userid, sessionid))
    conn.commit()
    conn.close()