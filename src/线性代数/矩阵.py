import torch

'''
正如向量将标量从零阶推⼴到⼀阶，矩阵将向量从⼀阶推⼴到⼆阶。矩阵，我们通常⽤粗体、⼤写字⺟来表
⽰（例如，X、Y和Z）
，在代码中表⽰为具有两个轴的张量。
数学表⽰法使⽤A ∈ Rm×n 来表⽰矩阵A，其由m⾏和n列的实值标量组成。我们可以将任意矩阵A ∈ Rm×n 视
为⼀个表格，其中每个元素aij 属于第i⾏第j列：
对于任意A ∈ Rm×n ，A的形状是（m,n）或m × n。当矩阵具有相同数量的⾏和列时，其形状将变为正⽅形；
因此，它被称为⽅阵（square matrix）。
当调⽤函数来实例化张量时，我们可以通过指定两个分量m和n来创建⼀个形状为m × n的矩阵。
'''

A = torch.arange(20).reshape(5,4)
print("打印举证: \n{}".format(A))

print(A.shape)
v = A.shape
print("x = {}, y = {}".format(v[0], v[1]))

# 打印矩阵函数
def print_matrix(matrix) :
    print("shape: {}, {}".format(matrix.shape[0], matrix.shape[1]))
    for x in range(0, matrix.shape[0]):
        for y in range(0, matrix.shape[1]):
            print("{:2} ".format(matrix[x][y]), end="")
        print()
    print()

print("打印矩阵")
print_matrix(A)

print("打印矩阵转置")
AT = A.T
print_matrix(AT)

'''
作为⽅阵的⼀种特殊类型，对称矩阵（symmetric matrix）A等于其转置：A = A⊤ 。这⾥定义⼀个对称矩阵B：
'''
B = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
print(B,"\n")

print("将B与它的转置进行比较")
print(B==B.T)

'''
矩阵是有⽤的数据结构：它们允许我们组织具有不同模式的数据。例如，我们矩阵中的⾏可能对应于不同的
房屋（数据样本）
，⽽列可能对应于不同的属性。曾经使⽤过电⼦表格软件或已阅读过 2.2节的⼈，应该对此
很熟悉。因此，尽管单个向量的默认⽅向是列向量，但在表⽰表格数据集的矩阵中，将每个数据样本作为矩
阵中的⾏向量更为常⻅。后⾯的章节将讲到这点，这种约定将⽀持常⻅的深度学习实践。例如，沿着张量的
最外轴，我们可以访问或遍历⼩批量的数据样本。
'''