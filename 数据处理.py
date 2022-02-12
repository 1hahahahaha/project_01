import pandas as pd
path=r'考试数据源（电量销售数据源）.csv'
f=pd.read_csv('考试数据源（电量销售数据源）.csv',encoding='utf-8')
#print(f)

#处理缺省值
#print(f.info())
#print(f.isna())
f1=f.dropna()
#print(f1.info())
#print(f1)

#处理重复值
#print(f1.duplicated())
#print(f1[f1.duplicated()])
f2=f1.drop_duplicates()
#print(f2[f2.duplicated()])

#处理异常值
#print(f2.describe())
f3=f2[f2['当期值']>0]
f4=f3[f3['当期值']<10000]
#print(f4)

#添加字段
date = pd.to_datetime(f4['统计时间'],format = '%Y-%m-%d')
#print(date)
year=date.dt.year
month=date.dt.month
day=date.dt.day
#print(year,month,day)
f5=f4.copy()
f5['年']=year
f5['月']=month
f5['日']=day
f5.to_csv('clear_data数据处理.csv',encoding='utf-8')


