import torch

A = torch.arange(20).reshape(5, 4)
x = torch.arange(4)
print("A = {}".format(A))
print("x = {}".format(x))
print("A.shape = {}".format(A.shape))
print("x.shape = {}".format(x.shape))
print("向量积： {}".format(torch.mv(A, x)))
