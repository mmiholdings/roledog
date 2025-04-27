
# Unified GENIE Intelligence Pipeline Scheduler

import subprocess
import schedule
import time

def run_pipeline():
    print("🔄 Running GENIE full-cycle pipeline...")
    subprocess.run(["python3", "generate_investment_mandate.py"])
    subprocess.run(["python3", "portfolio_rebalancer.py"])
    subprocess.run(["python3", "strategy_rebalancer.py"])
    subprocess.run(["python3", "sentiment_vix_overlay.py"])
    subprocess.run(["python3", "vix_vs_claude_alert.py"])
    subprocess.run(["python3", "claude_regime_classifier.py"])

# Schedule daily at 7 PM UTC
schedule.every().day.at("19:00").do(run_pipeline)

print("🧠 GENIE Pipeline Scheduler Active - Waiting for 19:00 UTC...")
while True:
    schedule.run_pending()
    time.sleep(30)
