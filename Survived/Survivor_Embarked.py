import matplotlib.pyplot as plt
import pandas as pd

"""
各登船港口的获救情况
"""
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

fig = plt.figure()
fig.set(alpha = 0.2)    #设定图表颜色alpha参数

data_train = pd.read_csv("E:/Python/Titanic-data-all/train.csv")

Survived_0 = data_train.Embarked[data_train.Survived == 0].value_counts()
Survived_1 = data_train.Embarked[data_train.Survived == 1].value_counts()
df = pd.DataFrame({u'获救': Survived_1, u'未获救': Survived_0})
df.plot(kind='bar', stacked=True)
plt.title(u"各登录港口乘客的获救情况")
plt.xlabel(u"登录港口")
plt.ylabel(u"人数")

plt.show()