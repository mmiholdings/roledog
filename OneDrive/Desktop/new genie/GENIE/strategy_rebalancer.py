
# MARL Strategy Rebalancer Based on Performance

import psycopg2

def rebalance_strategy():
    conn = psycopg2.connect(database="geniedb", user="genie", password="geniepass", host="localhost")
    cur = conn.cursor()
    cur.execute("SELECT strategy_name, sharpe_ratio FROM marl_strategy_scores ORDER BY sharpe_ratio DESC LIMIT 1;")
    best = cur.fetchone()[0]

    with open("active_strategy.txt", "w") as f:
        f.write(best)
    print("✅ Rebalanced to strategy:", best)

    cur.close()
    conn.close()

if __name__ == "__main__":
    rebalance_strategy()
