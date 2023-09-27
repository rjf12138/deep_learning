import torch

'''
标量、向量、矩阵和任意数量轴的张量（本⼩节中的“张量”指代数对象）有⼀些实⽤的属性。例如，从按
元素操作的定义中可以注意到，任何按元素的⼀元运算都不会改变其操作数的形状。同样，给定具有相同形
状的任意两个张量，任何按元素⼆元运算的结果都将是相同形状的张量。例如，将两个相同形状的矩阵相加，
会在这两个矩阵上执⾏元素加法。
'''

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = A.clone() # 通过分配新内存，将A的一个副本分配给B
print("张量相加: \n")
print("A: \n{}\n".format(A))
print("A + B: \n{}\n".format(A+B))


'''
具体⽽⾔，两个矩阵的按元素乘法称为Hadamard积（Hadamard product）
（数学符号⊙）
。对于矩阵B ∈ Rm×n ，
其中第i⾏和第j列的元素是bij 。矩阵A（在 (2.3.2)中定义）和B的Hadamard积为：
        |a11b11 a12b12  ... a1nb1n |
A * B = |a21b21 a22b22  ... a2nb2n |
        | ...    ...    ...  ...   |
        |am1bm1 am2bm2  ... amnbmn |
'''
print("A * B: \n{}\n".format(A * B))

'''
将张量乘以或加上⼀个标量不会改变张量的形状，其中张量的每个元素都将与标量相加或相乘。
'''
a = 2
X = torch.arange(24).reshape(2, 3, 4)
print("2 + X: \n{}\n".format(a + X))
print("(2 * X)'s shape: \n{}\n".format((a * X).shape))