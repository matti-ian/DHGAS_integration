import pandas as pd
import numpy as np

# Function to normalize data
def normalize_data(df):
    # Min-Max Normalization
    return (df - df.min()) / (df.max() - df.min())

# Load training data from text file
train_data_path = 'DHGAS\\data\\ecomm\\ecomm_edge_train.txt'
train_data = pd.read_csv(train_data_path, sep='\t', header=None)

# Load test data from text file
test_data_path = 'DHGAS\\data\\ecomm\\ecomm_edge_val_lr_train_test.txt'
test_data = pd.read_csv(test_data_path, sep='\t', header=None)

# Normalize training data
normalized_train_data = normalize_data(train_data)

# Normalize test data
normalized_test_data = normalize_data(test_data)

# Save normalized training data to new text file
normalized_train_data_path = 'normalized_train_data.txt'
normalized_train_data.to_csv(normalized_train_data_path, sep='\t', header=False, index=False)

# Save normalized test data to new text file
normalized_test_data_path = 'normalized_test_data.txt'
normalized_test_data.to_csv(normalized_test_data_path, sep='\t', header=False, index=False)

print("Normalization and saving completed.")
