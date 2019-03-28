import matplotlib.pyplot as plt
import pandas as pd

"""
看看各性别的获救情况
"""
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

fig = plt.figure()
fig.set(alpha = 0.2)    #设定图表颜色alpha参数

data_train = pd.read_csv("E:/Python/Titanic-data-all/train.csv")
Survived_m = data_train.Survived[data_train.Sex == 'male'].value_counts()
Survived_f = data_train.Survived[data_train.Sex == 'female'].value_counts()
df = pd.DataFrame({u'男性':Survived_m, u'女性':Survived_f})
df.plot(kind='bar', stacked = True)
plt.title(u'按性别看获救情况(1为获救)')
plt.xlabel(u'性别')
plt.ylabel(u'人数')
plt.show()