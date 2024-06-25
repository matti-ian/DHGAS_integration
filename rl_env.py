# rl_env.py
import gym
from gym import spaces
import numpy as np

class CustomEnv(gym.Env):
    def __init__(self, train_data):
        super(CustomEnv, self).__init__()
        self.train_data = train_data
        self.current_step = 0
        self.observation_space = spaces.Box(low=np.min(train_data), high=np.max(train_data), shape=(4,), dtype=np.float32)
        self.action_space = spaces.Discrete(2)

    def reset(self):
        self.current_step = 0
        return self.train_data[self.current_step]

    def step(self, action):
        self.current_step += 1
        if self.current_step >= len(self.train_data):
            done = True
            reward = 0
            obs = np.zeros(4)
        else:
            done = False
            reward = 1  # Example reward
            obs = self.train_data[self.current_step]
        return obs, reward, done, {}

    def render(self, mode='human'):
        pass
