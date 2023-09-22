import torch
import os
import pandas as pd
import numpy as np

file_path = "../../output/debug/bin/house_tiny.csv"
data = pd.read_csv(file_path)

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = inputs.fillna(inputs.mean(numeric_only=True))
inputs = pd.get_dummies(inputs, dummy_na=True, dtype=float)
print("inputs")
print(inputs)

print("output")
print(outputs)

X, y = torch.tensor(inputs.values), torch.tensor(outputs.values)
print(X)
print(y)