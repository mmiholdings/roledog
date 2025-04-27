
import pandas as pd
from stable_baselines3 import PPO
from trading_env import SmartFlowEnv

def retrain_agent(log_file="trade_log.csv"):
    df = pd.read_csv(log_file)
    env = SmartFlowEnv(df)
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=50000)
    model.save("retrained_agent")
    print("✅ Agent retrained and saved.")

if __name__ == "__main__":
    retrain_agent()
