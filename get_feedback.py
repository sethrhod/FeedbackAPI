import psycopg2

def get_feedback(userid):
    conn = psycopg2.connect("dbname=test user=postgres")
    cur = conn.cursor()
    cur.execute("SELECT * FROM feedback WHERE userid = %s", (userid))
    rows = cur.fetchall()
    for row in rows:
        {
            "userid": row[0],
            "sessionid": row[1],
            "feedback": row[2]
        }
    conn.close()
    return rows