import torch

'''
范数听起来很像距离的度量。欧⼏⾥得距离和毕达哥拉斯定理中的⾮负性概念和三⻆不等式可能会给出⼀些
启发。事实上，欧⼏⾥得距离是⼀个L2 范数：假设n维向量x中的元素是x1 , . . . , xn ，其L2 范数是向量元素平
⽅和的平⽅根
'''
u = torch.tensor([3.0, -4.0])
print("u = {}".format(u))
print("范数：{}".format(torch.norm(u)))