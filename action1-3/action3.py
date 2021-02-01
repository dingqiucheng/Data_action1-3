# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:44:04 2021

@author: VAS6150C
"""


import pandas as pd
from pandas import Series,DataFrame

data = pd.read_csv('car_complain.csv')
#处理投诉类型
data = data.drop('problem',axis=1).join(data.problem.str.get_dummies(','))

#品牌投诉统计,及清洗
def f(x):
    x = x.replace('一汽-大众','一汽大众')
    return x
data['brand']=data['brand'].apply(f)

result = data.groupby(['brand'])['id'].agg(['count'])
print(result)

tags = data.columns[7:]
tags

result2 = data.groupby(['brand'])[tags].agg(['sum'])
print(result2)

result2 = result.merge(result2,left_index=True,right_index=True,how='left')
result2 = result2.sort_values('count',ascending=False)
print(result2)
result2.to_csv('result_brand.csv')







