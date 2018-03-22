import pandas as pd

#Series是一维的数组，通过index可以设置索引
s = pd.Series([1,2,3], index=['a','b','c'])

#DataFrame是二维数据
# 带 Series 的字典
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)  # 新建 DataFrame

# 列表构成的字典
d = {'one' : [1, 2, 3, 4], 'two' : [4, 3, 2, 1]}
df1 = pd.DataFrame(d) # 未指定索引
df2 = pd.DataFrame(d, index=['a', 'b', 'c', 'd']) # 指定索引

#二维情况下索引名表示选择列
# print(df2['one'])

#列的删除/增加
df2.pop('one')
# print(df2)
df2.insert(1,'three', [1,2,3,4])
print(df2)

