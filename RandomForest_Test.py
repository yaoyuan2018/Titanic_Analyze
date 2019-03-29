from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import pandas as pd

##使用 RadomForestClassifier 填补缺失的年龄属性
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

fig = plt.figure()
fig.set(alpha = 0.2)    #设定图标颜色alpha参数

data_train = pd.read_csv("E:/Python/Titanic-data-all/train.csv")

def set_missing_ages(df):

    #把已有的数值型特征取出来丢进Random Forest Regressor中
    age_df = df[['Age', 'Fare', 'Parch', 'SibSp', 'Pclass']]

    #乘客分成已知年龄和未知年龄两部分
    known_age = age_df[age_df.Age.notnull()].as_matrix()
    unknown_age = age_df[age_df.Age.isnull()].as_matrix()

    # y即目标年龄
    y = known_age[:, 0]

    # x即特征属性值
    X = known_age[:, 1]

    # fit到RandomForestRegressor之中
    rfr = RandomForestRegressor(random_state = 0, n_estimators = 2000, n_jobs = -1)
    rfr.fit(X,y)

    # 用得到的模型进行未知年龄结果预测
    predictedAges = rfr.predict(unknown_age[:, 1::])

    # 用得到的预测结果填补原缺失数据
    df.loc[(df.Age.isnull()), 'Age'] = predictedAges

    return df, rfr

def set_Cabin_type(df):
    df.loc[(df.Cabin.notnull()), 'Cabin'] = "Yes"
    df.loc[(df.Cabin.notnull()), 'Cabin'] = "NO"
    return df

data_train, rfr = set_missing_ages(data_train)
data_train = set_Cabin_type(data_train)

