# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:04:02 2021

@author: dingqiucheng
"""

import pandas as pd
from pandas import Series,DataFrame
data = {'语文':[68,95,98,90,80],
        '数学':[65,76,86,88,90],
        '英语':[30,98,88,77,90]}
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data,index = ['张飞','关羽','刘备','典韦','许褚'])
print(df1)
print(df2)

#平均分
print('平均分\n',df2.mean())
#最小成绩
print('最小成绩\n',df2.min())
#最大成绩
print('最大成绩\n',df2.max())
#方差
print('方差\n',df2.var())
#标准差
print('标准差\n',df2.std())
#多个统计
print(df2.describe())

df2['总成绩']=df2.apply(lambda i:i.sum(),axis=1)
print(df2.sort_values('总成绩',ascending=False))