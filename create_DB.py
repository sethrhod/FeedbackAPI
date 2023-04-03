import psycopg2

def create_DB():
    conn = psycopg2.connect("dbname=test user=postgres")
    cur = conn.cursor()
    cur.execute("CREATE TABLE if NOT EXISTS feedback (userid uuid, sessionid uuid, feedback VARCHAR(255))")
    conn.commit()
    conn.close()