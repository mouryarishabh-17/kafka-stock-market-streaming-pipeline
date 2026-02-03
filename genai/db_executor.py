import psycopg2

def run_query(sql: str):
    conn = psycopg2.connect(
        dbname="market_data",
        user="spark_user",
        password="spark_pass",
        host="127.0.0.1",   # MUST be 127.0.0.1
        port="5432"
    )

    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows
