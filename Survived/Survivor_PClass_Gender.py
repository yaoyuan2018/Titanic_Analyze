import matplotlib.pyplot as plt
import pandas as pd
#各种舱级别情况下个性别的获救情况

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

fig = plt.figure()
fig.set(alpha = 0.65)    #设置图像透明度
data_train = pd.read_csv("E:/Python/Titanic-data-all/train.csv")

plt.title(u"根据舱等级和性别的获救情况")

ax1 = fig.add_subplot(141)  #??
data_train.Survived[data_train.Sex == 'female'][data_train.Pclass != 3].value_counts().plot(kind = 'bar', label = "female high_class", color = '#FA2479')
ax1.set_xticklabels([u"获救", u"未获救"], rotation = 0)
ax1.legend([u"女性/高级舱"], loc = 'best')

ax2 = fig.add_subplot(142, sharey = ax1)
data_train.Survived[data_train.Sex == 'female'][data_train.Pclass == 3].value_counts().plot(kind = 'bar', label = 'female, low_class', color = 'pink')
ax2.set_xticklabels([u"未获救", u"获救"], rotation = 0)
plt.legend([u"女性/低级舱"], loc = 'best')

ax3 = fig.add_subplot(143, sharey = ax1)
data_train.Survived[data_train.Sex == 'male'][data_train.Pclass != 3].value_counts().plot(kind = 'bar', label = 'male, high_class', color = 'lightblue')
ax3.set_xticklabels([u"未获救", u"获救"], rotation = 0)
plt.legend([u"男性/高级舱"], loc = 'best')

ax4 = fig.add_subplot(144, sharey = ax1)
data_train.Survived[data_train.Sex == 'male'][data_train.Pclass == 3].value_counts().plot(kind = 'bar', label = 'male, low_class', color = 'steelblue')
ax4.set_xticklabels([u"未获救", u"获救"], rotation = 0)
plt.legend([u"男性/低级舱"], loc = 'best')

plt.show()