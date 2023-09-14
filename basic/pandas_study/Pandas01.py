import pandas as pd
import numpy as np

# Series
a = pd.Series({'a':1, 'b':2, 'c':3})
print(a)
print(a.index.values)

a = np.arange(1, 5)
b = pd.Series(a)
print(b)
print("=" * 200)

a1 = np.array(["a","b","c"])
b1 = pd.Series(a1)
print(b1)
print(b1.index)
print(b1.index.values)
print("=" * 200)

a2 = np.array([1, 2, 3, 4])
b2 = pd.Series(a2)
print(b2)
print(b2.index)
print(b2.index.values)
print("=" * 200)


# DataFrame
a3 = {'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9]}
b3 = pd.Series(a3)
c3 = pd.DataFrame(a3, index=a3.keys())
print(b3)
print(c3)
print(c3.index.values)
print(c3.columns)

a4 = pd.DataFrame({'a':(1,2), 'b':1, 'c':3})
print(a4)
a4.index=["x",'y']
a4.columns=['i','j','k']
print(a4)

print(a4.loc['x']) # location
print(a4.loc[a4["i"] == 2]) # 조건 설정 가능
print(a4.iloc[0]) # index_location

a5 = {'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9], 'd':[10,11,12]}
b5 = pd.DataFrame(a5)
print(b5.describe())

print(b5.sum()) # 열 합하기
print(b5.sum(axis=1)) # 행 합하기
print(b5.min)
print(b5.min(axis=1))
print(b5.max)
print(b5.mean)
print(b5.std(), b5.var()) # 표준편차, 분산
