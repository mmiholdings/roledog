import pandas as pd
import os

def fetch_mes_data():
    # Simulate MES futures data (QC-style)
    date_rng = pd.date_range(start='2024-01-01', end='2024-01-30', freq='5T')
    df = pd.DataFrame(date_rng, columns=['timestamp'])
    df['close'] = 5200 + (df.index % 50) * 0.25
    df.to_csv("qc_data/mes_sample.csv", index=False)
    print("✅ MES data saved to qc_data/mes_sample.csv")

if __name__ == "__main__":
    os.makedirs("qc_data", exist_ok=True)
    fetch_mes_data()
