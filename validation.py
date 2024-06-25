# validate_rl.py

import torch
import yaml
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from integrated_model import IntegratedModel
import gym
from gym import spaces

# Load configuration
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Load test data
test_data = []
with open('normalized_test_data.txt', 'r') as f:
    for line in f:
        numbers = [float(x) for x in line.split()]
        test_data.append(numbers)

test_data = torch.tensor(test_data, dtype=torch.float32)

# Define custom environment
class CustomEnv(gym.Env):
    def __init__(self, data, model):
        super(CustomEnv, self).__init__()
        self.data = data
        self.model = model
        self.current_step = 0
        self.action_space = spaces.Discrete(2)  # Define action space, e.g., discrete actions
        self.observation_space = spaces.Box(low=-float('inf'), high=float('inf'), shape=(4,), dtype=torch.float32)  # Define observation space

    def reset(self):
        self.current_step = 0
        return self.data[self.current_step]

    def step(self, action):
        self.current_step += 1
        done = self.current_step >= len(self.data)
        reward = 1.0  # Define reward logic
        next_state = self.data[self.current_step] if not done else self.data[0]
        return next_state, reward, done, {}

# Initialize environment and model
env = DummyVecEnv([lambda: CustomEnv(test_data, IntegratedModel(config))])
model = PPO.load("ppo_integrated_model")
print("Model loaded from 'ppo_integrated_model'.")

# Evaluate the model
print("Starting evaluation...")
obs = env.reset()
total_rewards = 0
step_count = 0
done = False

while not done:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    total_rewards += reward
    step_count += 1
    if step_count % 100 == 0:
        print(f"Step: {step_count}, Total Rewards: {total_rewards}")

print(f"Total Test Rewards: {total_rewards}")
