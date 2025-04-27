import psycopg2
import json
from datetime import datetime

def log_trade_to_postgres(trade):
    conn = psycopg2.connect(
        dbname="geniedb",
        user="genie",
        password="geniepass",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    query = """
        INSERT INTO trade_logs (timestamp, broker, symbol, side, qty, price, status, latency)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(query, (
        datetime.utcnow(),
        trade["broker"],
        trade["symbol"],
        trade["side"],
        trade["qty"],
        trade["price"],
        trade["status"],
        trade["latency"]
    ))
    conn.commit()
    cur.close()
    conn.close()