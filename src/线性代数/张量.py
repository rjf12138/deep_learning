import torch

'''
就像向量是标量的推⼴，矩阵是向量的推⼴⼀样，我们可以构建具有更多轴的数据结构。张量（本⼩节中的
“张量”指代数对象）是描述具有任意数量轴的n维数组的通⽤⽅法。例如，向量是⼀阶张量，矩阵是⼆阶张
量。张量⽤特殊字体的⼤写字⺟表⽰（例如，X、Y和Z）
，它们的索引机制（例如xijk 和[X]1,2i−1,3 ）与矩阵类似。
当我们开始处理图像时，张量将变得更加重要，图像以n维数组形式出现，其中3个轴对应于⾼度、宽度，以
及⼀个通道（channel）轴，⽤于表⽰颜⾊通道（红⾊、绿⾊和蓝⾊）
。现在先将⾼阶张量暂放⼀边，⽽是专
注学习其基础知识。
'''

X = torch.arange(24).reshape(2, 3, 4)
print(X)

