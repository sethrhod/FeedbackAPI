import psycopg2

def get_feedback(uuid):
    conn = psycopg2.connect("dbname=test user=postgres")
    cur = conn.cursor()
    # cur.execute("SELECT * FROM users WHERE uuid = %s", (uuid,))
    # rows = cur.fetchall()
    # print(rows)
    # for row in rows:
    #     print("uuid = ", row[0])
    #     print("sessionid = ", row[1])
    #     print("feedback = ", row[2], "\n")

    # print("Operation done successfully")
    conn.close()