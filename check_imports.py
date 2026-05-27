import torch

print("START")
print("torch:", torch.__version__)
print("cuda available:", torch.cuda.is_available())

import torchvision
print("torchvision OK")

import torch_scatter
print("torch_scatter OK")

import torch_geometric
print("torch_geometric OK")

import lightning
print("lightning OK")

import wandb
print("wandb OK")

import pandas
print("pandas OK")

print("ALL IMPORTS OK")
