
# MARL-Driven Portfolio Rebalancer

import psycopg2

def rebalance_portfolio():
    conn = psycopg2.connect(database="geniedb", user="genie", password="geniepass", host="localhost")
    cur = conn.cursor()
    cur.execute("SELECT symbol, avg_pnl, win_rate FROM agent_strategy_performance ORDER BY win_rate DESC LIMIT 5;")
    top_assets = cur.fetchall()

    # Simple rebalance: allocate 50% to top 3 strategies
    allocations = {}
    weights = [0.25, 0.15, 0.10]
    for i, row in enumerate(top_assets[:3]):
        allocations[row[0]] = weights[i]

    print("✅ Portfolio Rebalanced:", allocations)
    cur.close()
    conn.close()

if __name__ == "__main__":
    rebalance_portfolio()
