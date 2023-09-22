import os
import pandas as pd
import numpy as np

'''
注意，
“NaN”项代表缺失值。为了处理缺失的数据，典型的⽅法包括插值法和删除法，其中插值法⽤⼀个替
代值弥补缺失值，⽽删除法则直接忽略缺失值。在这⾥，我们将考虑插值法。
通过位置索引iloc，我们将data分成inputs和outputs，其中前者为data的前两列，⽽后者为data的最后⼀列。
对于inputs中缺少的数值，我们⽤同⼀列的均值替换“NaN”项。
'''

file_path = "../../output/debug/bin/house_tiny.csv"
data = pd.read_csv(file_path)

print(data)

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
#设置参数`numeric_only=True`。这样会忽略DataFrame中的非数值列，并计算其他列的平均值
#将计算出来的平均值填充到其他行
inputs = inputs.fillna(inputs.mean(numeric_only=True))

print(inputs)

'''
对于inputs中的类别值或离散值，我们将“NaN”视为⼀个类别。由于“巷⼦类型”（“Alley”）列只接受两
种类型的类别值“Pave”和“NaN”
，pandas可以⾃动将此列转换为两列“Alley_Pave”和“Alley_nan”
。巷
⼦类型为“Pave”的⾏会将“Alley_Pave”的值设置为1，“Alley_nan”的值设置为0。缺少巷⼦类型的⾏会
将“Alley_Pave”和“Alley_nan”分别设置为0和1。
'''

inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)