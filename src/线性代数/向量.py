import torch

'''
向量可以被视为标量值组成的列表。这些标量值被称为向量的元素（element）或分量（component）
。当向
量表⽰数据集中的样本时，它们的值具有⼀定的现实意义。例如，如果我们正在训练⼀个模型来预测贷款违
约⻛险，可能会将每个申请⼈与⼀个向量相关联，其分量与其收⼊、⼯作年限、过往违约次数和其他因素相
对应。如果我们正在研究医院患者可能⾯临的⼼脏病发作⻛险，可能会⽤⼀个向量来表⽰每个患者，其分量
为最近的⽣命体征、胆固醇⽔平、每天运动时间等。在数学表⽰法中，向量通常记为粗体、⼩写的符号（例
如，x、y和z)）
。
⼈们通过⼀维张量表⽰向量。⼀般来说，张量可以具有任意⻓度，取决于机器的内存限制。
'''

x = torch.arange(4)
print(x)

print("打印向量中的每个元素")
for i in range(0, len(x)):
    print(x[i], end=" ")
print()

'''
向量只是⼀个数字数组，就像每个数组都有⼀个⻓度⼀样，每个向量也是如此。在数学表⽰法中，如果我们想
说⼀个向量x由n个实值标量组成，可以将其表⽰为x ∈ Rn 。向量的⻓度通常称为向量的维度（dimension）
。
与普通的Python数组⼀样，我们可以通过调⽤Python的内置len()函数来访问张量的⻓度。
'''
print("打印向量的长度: {}".format(len(x)))

'''
当⽤张量表⽰⼀个向量（只有⼀个轴）时，我们也可以通过.shape属性访问向量的⻓度。形状（shape）是⼀
个元素组，列出了张量沿每个轴的⻓度（维数）
。对于只有⼀个轴的张量，形状只有⼀个元素。
'''

print("打印.shape: {}".format(x.shape))

'''
请注意，维度（dimension）这个词在不同上下⽂时往往会有不同的含义，这经常会使⼈感到困惑。为了清楚
起⻅，我们在此明确⼀下：向量或轴的维度被⽤来表⽰向量或轴的⻓度，即向量或轴的元素数量。然⽽，张
量的维度⽤来表⽰张量具有的轴数。在这个意义上，张量的某个轴的维数就是这个轴的⻓度
'''