# 넘파이(Numpy)
# 고성능(대량)의 수치 계산을 위한 라이브러리
# 벡터, 행렬 연산
import numpy as np

# 기존 방식
numArray1 = [1, 2, 3, 4, 5]
numArray2 = [6, 7, 8, 9, 10]

numArray3 = []
for i in range(len(numArray1)):
    numArray3.append(numArray1[i] + numArray2[i])

print(numArray3)
print("=" * 200)

# numpy_study 적용
npArray1 = np.array(numArray1)
npArray2 = np.array(numArray2)
npArray3 = npArray1 * npArray2

print(npArray1)
print(npArray2)
print(npArray3)
print("=" * 200)

# 2차원 배열
npDoubleArray1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
npDoubleArray2 = np.array([[11,12,13,14,15], [16,17,18,19,20]])
print(npDoubleArray1)
print(npDoubleArray2)
print(npDoubleArray1+npDoubleArray2)
print("=" * 200)

# np참조 활용
print(npArray1.shape) # 크기
print(npDoubleArray1.shape)

npArray4 = np.arange(10) # 배열 0부터 자동 생성
print(npArray4)
npArray5 = np.arange(1, 11) # 범위 지정하여 자동 생성
print(npArray5)
npArray6 = np.zeros(10) # 배열을 모두 0으로 생성
print(npArray6)
npArray7 = np.zeros_like(npDoubleArray1) # 배열의 형태를 복사하여 모두 0으로 채움
print(npArray7)
npArray8 = np.ones(10) # 배열을 모두 1으로 생성
print(npArray8)
npArray9 = np.ones_like(npDoubleArray1) # 배열의 형태를 복사하여 모두 0으로 채움
print(npArray9)
npArray10 = np.full((5, 3), 5) # ((행, 열), 인덱스데이터)로 배열을 생성
print(npArray10)

print(npArray10 * 2) # 모든 행, 열에 연산작업 가능