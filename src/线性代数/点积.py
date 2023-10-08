import torch

'''
我们已经学习了按元素操作、求和及平均值。另⼀个最基本的操作之⼀是点积。给定两个向量x, y ∈ Rd ，它
们的点积（dot product）x⊤ y （或⟨x, y⟩）是相同位置的按元素乘积的和：x⊤ y = i=1 xi yi 。
'''
x = torch.arange(4, dtype=torch.float32)
y = torch.ones(4, dtype= torch.float32)
print("x={}".format(x))
print("y={}".format(y))
print("点积：{}".format(torch.dot(x, y)))

'''
我们可以通过执⾏按元素乘法，然后进⾏求和来表⽰两个向量的点积：
'''

print("按元素乘法求和：{}".format(torch.sum(x * y)))

'''
点积在很多场合都很有⽤。例如，给定⼀组由向量x ∈ Rd 表⽰的值，和⼀组由w
根据权重w的加权和，可以表⽰为点积x⊤ w。当权重为⾮负数且和为1（即
时，点积表⽰加
权平均（weighted average）
。将两个向量规范化得到单位⻓度后，点积表⽰它们夹⻆的余弦。本节后⾯的内
容将正式介绍⻓度（length）的概念。
'''