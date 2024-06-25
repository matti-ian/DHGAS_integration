import gym
from gym import spaces
import numpy as np
import torch

class CustomEnv(gym.Env):
    def __init__(self, data, model):
        super(CustomEnv, self).__init__()
        self.data = data
        self.model = model
        self.current_step = 0

        # Define action and observation space
        # Example: a 4-dimensional continuous observation space
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(4,), dtype=np.float32)

        # Example: a discrete action space of size 2
        self.action_space = spaces.Discrete(2)

    def reset(self):
        self.current_step = 0
        return self.data[self.current_step]

    def step(self, action):
        self.current_step += 1
        done = self.current_step >= len(self.data)
        reward = 1 if not done else 0
        obs = self.data[self.current_step] if not done else np.zeros(4)
        
        # Forward pass through the model
        model_output = self.model(torch.tensor(obs, dtype=torch.float32))
        
        
        # Example: derive reward or any other information from model output if necessary
        # Adjust the reward based on model output if needed

        return obs, reward, done, {}

    def render(self, mode='human'):
        pass
