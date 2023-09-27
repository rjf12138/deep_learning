import torch

'''
我们可以对任意张量进⾏的⼀个有⽤的操作是计算其元素的和。数学表⽰法使⽤ 符号表⽰求和。为了表⽰
∑d
⻓度为d的向量中元素的总和，可以记为 i=1 xi 。在代码中可以调⽤计算求和的函数：
'''
x = torch.arange(4, dtype=torch.float32)
print("x: {}\nx.sum: {}\n".format(x, x.sum()))

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
print("A: \n{}\n".format(A))
print("A's shape: {}\nA.sum: {}\n".format(A.shape, A.sum()))

'''
默认情况下，调⽤求和函数会沿所有的轴降低张量的维度，使它变为⼀个标量。我们还可以指定张量沿哪⼀
个轴来通过求和降低维度。以矩阵为例，为了通过求和所有⾏的元素来降维（轴0），可以在调⽤函数时指
定axis=0。由于输⼊矩阵沿0轴降维以⽣成输出向量，因此输⼊轴0的维数在输出形状中消失。
'''

A_sum_axis0 = A.sum(axis=0)
print("A_sum_axis0: {}\nA_sum_axis0.shape: {}\n".format(A_sum_axis0, A_sum_axis0.shape))

'''
沿着⾏和列对矩阵求和，等价于对矩阵的所有元素进⾏求和。
'''
A.sum(axis=[0, 1]) # 结果和A.sum()相同
print("A.sum(axis=[0, 1]): {}\n".format(A.sum(axis=[0, 1])))

'''
⼀个与求和相关的量是平均值（mean或average）。我们通过将总和除以元素总数来计算平均值。在代码中，
我们可以调⽤函数来计算任意形状张量的平均值。
'''
print("A.mean(): {}".format(A.mean()))
print("A.sum() / A.numel(): {}\n".format(A.sum() / A.numel()))

'''
同样，计算平均值的函数也可以沿指定轴降低张量的维度。
'''
print("A.mean(axis=0): {}".format(A.mean(axis=0)))
print("A.sum(axis=0) / A.shape(0): {}\n".format(A.sum(axis=0) / A.shape[0]))

'''
但是，有时在调⽤函数来计算总和或均值时保持轴数不变会很有⽤。
'''
sum_A = A.sum(axis=1, keepdim=True)
print("sum_A: {}\n".format(sum_A))

'''
例如，由于sum_A在对每⾏进⾏求和后仍保持两个轴，我们可以通过⼴播将A除以sum_A。
'''
print("A / sum_A: \n{}\n".format(A / sum_A))

'''
如果我们想沿某个轴计算A元素的累积总和，⽐如axis=0（按⾏计算）
，可以调⽤cumsum函数。此函数不会沿
任何轴降低输⼊张量的维度。
'''
print("A.cumsum(axis=0): \n{}\n".format(A.cumsum(axis=0)))