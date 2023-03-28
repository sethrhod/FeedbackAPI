from user_Class import User
import psycopg2

def submit_feedback(uuid, sessionid, feedback):
    conn = psycopg2.connect("dbname=test user=postgres")
    cur = conn.cursor()
    # cur.execute("SUBMIT * FROM users WHERE uuid = %s", (uuid,))
