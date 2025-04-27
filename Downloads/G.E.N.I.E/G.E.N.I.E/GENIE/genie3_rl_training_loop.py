
from stable_baselines3 import PPO
from trading_env import TradingEnv
import gym

class GENIEMarketEnv(TradingEnv):
    def __init__(self):
        super().__init__()
        self.action_space = gym.spaces.Discrete(3)
        self.observation_space = gym.spaces.Box(low=-1, high=1, shape=(8,), dtype=float)

    def step(self, action):
        # Apply action logic here
        return self._next_state(), reward, done, {}

env = GENIEMarketEnv()
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100000)
model.save("genie3_marl_agent")
