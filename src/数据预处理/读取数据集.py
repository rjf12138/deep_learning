import os
import pandas as pd

'''
在Python中常⽤的数据分析⼯具中，我们通常使⽤pandas软件包。像庞⼤的Python⽣态系统中
的许多其他扩展包⼀样，pandas可以与张量兼容。本节我们将简要介绍使⽤pandas预处理原始数据，并将原
始数据转换为张量格式的步骤。后⾯的章节将介绍更多的数据预处理技术。

我们⾸先创建⼀个⼈⼯数据集，并存储在CSV（逗号分隔值）⽂件 ../../output/debug/bin/house_tiny.csv中。
以其他格式存储的数据也可以通过类似的⽅式进⾏处理。下⾯我们将数据集按⾏写⼊CSV⽂件中
'''
file_path = "../../output/debug/bin/house_tiny.csv"

data_file = os.path.join(file_path)
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n') # 列名
    f.write('NA,Pave,127500\n') # 每⾏表⽰⼀个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')

data = pd.read_csv(file_path)
print(data)