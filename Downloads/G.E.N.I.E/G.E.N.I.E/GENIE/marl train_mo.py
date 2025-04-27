import json
from stable_baselines3 import PPO
from stable_baselines3.common.envs import DummyVecEnv
import gym
import numpy as np
import os

class MESReplayEnv(gym.Env):
    def __init__(self, buffer_file="buffer/mes_buffer.json"):
        super(MESReplayEnv, self).__init__()
        with open(buffer_file) as f:
            self.buffer = json.load(f)
        self.index = 0
        self.observation_space = gym.spaces.Box(low=0, high=10000, shape=(1,), dtype=np.float32)
        self.action_space = gym.spaces.Discrete(2)

    def reset(self):
        self.index = 0
        return np.array(self.buffer[self.index][0], dtype=np.float32)

    def step(self, action):
        state, act, reward, next_state, done = self.buffer[self.index]
        reward = reward if act == action else -abs(reward)
        self.index += 1
        if self.index >= len(self.buffer):
            done = True
        return np.array(next_state, dtype=np.float32), reward, done, {}

env = DummyVecEnv([lambda: MESReplayEnv()])
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=1000)
model.save("ppo_mo_agent")

print("✅ MARL PPO Agent trained and saved as ppo_mo_agent.zip")
