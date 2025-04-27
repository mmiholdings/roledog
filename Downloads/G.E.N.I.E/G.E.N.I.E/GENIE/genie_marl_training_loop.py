
from stable_baselines3 import PPO
from trading_env import SmartFlowEnv

env = SmartFlowEnv()  # Custom Gym env using SmartFlow/Claude state vector
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100_000)
model.save("genie_marl_smartflow")
