import torch


'''
在数学表⽰法中，我们将通过符号f : R → R 来表⽰⼀元标量运算符（只接收⼀个输⼊）。这意味着该函数
从任何实数（R）映射到另⼀个实数。同样，我们通过符号f : R, R → R 表⽰⼆元标量运算符，这意味着该
函数接收两个输⼊，并产⽣⼀个输出。给定同⼀形状的任意两个向量u和v和⼆元运算符f ，我们可以得到向
量c = F (u, v)。具体计算⽅法是ci ← f (ui , vi )，其中ci 、ui 和vi 分别是向量c、u和v中的元素。在这⾥，我们
通过将标量函数升级为按元素向量运算来⽣成向量值 F : Rd , Rd → Rd 。
对于任意具有相同形状的张量，常⻅的标准算术运算符（+、-、*、/和**）都可以被升级为按元素运算。我
们可以在同⼀形状的任意两个张量上调⽤按元素操作。在下⾯的例⼦中，我们使⽤逗号来表⽰⼀个具有5个
元素的元组，其中每个元素都是按元素操作的结果。
'''

x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 3, 2, 2])

print("x = ", end="")
print(x)

print("y = ", end="")
print(y)

print("x + y = ", end="")
print(x+y)

print("x - y = ", end="")
print(x-y)

print("x * y = ", end="")
print(x*y)

print("x / y = ", end="")
print(x/y)

# x 里元素对应 y 中元素的幂次，比如[1^2, 2^3, 4^2, 8^2]
print("x ** y = ", end="")
print(x ** y)

# “按元素”⽅式可以应⽤更多的计算，包括像求幂这样的⼀元运算符。开根号
e = torch.exp(x)
print("exp(x) = ", end="")
print(e)

'''
我们也可以把多个张量连结（concatenate）在⼀起，把它们端对端地叠起来形成⼀个更⼤的张量。我们只需
要提供张量列表，并给出沿哪个轴连结。下⾯的例⼦分别演⽰了当我们沿⾏（轴-0，形状的第⼀个元素）和按
列（轴-1，形状的第⼆个元素）连结两个矩阵时，会发⽣什么情况。我们可以看到，第⼀个输出张量的轴-0⻓
度（6）是两个输⼊张量轴-0⻓度的总和（3 + 3）
；第⼆个输出张量的轴-1⻓度（8）是两个输⼊张量轴-1⻓度
的总和（4 + 4）。
'''
X = torch.arange(12, dtype=torch.float32).reshape((3,4))
print(X)

Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(Y)

dim0 = torch.cat((X, Y), dim=0)
dim1 = torch.cat((X, Y), dim=1)
print(dim0)
print(dim1)

# 我们想通过逻辑运算符构建⼆元张量。以X == Y为例：对于每个位置，如果X和Y在该位置相等，则新
# 张量中相应项的值为1。这意味着逻辑语句X == Y在该位置处为真，否则该位置为0。
B = (X == Y)
print(B)

# 对张量中的所有元素进⾏求和，会产⽣⼀个单元素张量。
sum = X.sum()
print(sum)