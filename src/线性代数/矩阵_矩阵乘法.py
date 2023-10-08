import torch

A = torch.arange(20, dtype=torch.long).reshape(5, 4)
B = torch.ones(4, 3, dtype=torch.long)
print("A = \n{}".format(A))
print("B = \n{}".format(B))
print("矩阵乘法：\n{}".format(torch.mm(A, B)))