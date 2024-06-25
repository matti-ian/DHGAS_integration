# train_rl.py

import torch
import yaml
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from integrated_model import IntegratedModel
from rl_env import CustomEnv
import gym

# Load configuration
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Load train data
train_data = []
with open('normalized_train_data.txt', 'r') as f:
    for line in f:
        numbers = [float(x) for x in line.split()]
        train_data.append(numbers)

train_data = torch.tensor(train_data, dtype=torch.float32)

# Initialize environment and model
env = DummyVecEnv([lambda: CustomEnv(train_data, IntegratedModel(config))])
model = PPO("MlpPolicy", env, verbose=1)

# Train the model
print("Starting training...")

batch_size = 32
num_batches = len(train_data) // batch_size

for epoch in range(config['commformer_params']['num_epochs']):
    for i in range(num_batches):
        batch_data = train_data[i * batch_size:(i + 1) * batch_size]
        env = DummyVecEnv([lambda: CustomEnv(batch_data, IntegratedModel(config))])
        model.set_env(env)
        model.learn(total_timesteps=batch_size)
        print(f"Epoch: {epoch + 1}, Batch: {i + 1}/{num_batches} completed.")

print("Training completed.")

# Save the model
model.save("ppo_integrated_model")
print("Model saved as 'ppo_integrated_model'.")
