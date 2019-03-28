import matplotlib.pyplot as plt
import pandas as pd
#有无堂兄弟姐妹的/孩子/父母的获救情况

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

fig = plt.figure()
fig.set(alpha = 0.65)    #设置图像透明度
data_train = pd.read_csv("E:/Python/Titanic-data-all/train.csv")

g = data_train.groupby(['SibSp', 'Survived'])
df = pd.DataFrame(g.count()['PassengerId'])
print(df)

c = data_train.Cabin.value_counts()
# df = pd.DataFrame(c.count()['PassengerId'])
print(c)