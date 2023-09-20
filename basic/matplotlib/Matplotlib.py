import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
font_list = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
for font in font_list:
    print(font)
rc('font', family='D2Coding')
# 색상 및 기타 정보
# https://matplotlib.org/stable/gallery/color/named_colors.html


# data 시각화 모듈
x = [1,2,3,4]
y = [2,3,4,5]

#1
plt.plot(x, y)
plt.show()
#2
plt.bar(x, y)
plt.show()

#3
figure = plt.figure() # 그래프 테두리
axes = figure.add_subplot(111)

x2 = np.array(x)
y2 = np.array([4,1,3,6])

axes.plot(x,y, color='red', linestyle='dashed', marker='^')
axes.plot(x2,y2, color='k', linestyle='dotted', marker='o')
plt.show()

#4
figure = plt.figure()
axes1 = figure.add_subplot(121) # 1행 2열에서 1열
axes1.plot(x, y)
axes2 = figure.add_subplot(122) # 1행 2열에서 2열
axes2.plot(x2, y2)
plt.show()

#5
figure = plt.figure()
axes = figure.add_subplot(111)

axes.bar(x, y)
axes.bar(x2, y2)
plt.show()

#6
figure = plt.figure()
axes = figure.add_subplot(111)
axes1 = axes.twinx()
axes.bar(x, y, color="blue", label="bar")
axes1.plot(x2, y2, color='red', label='plot')
plt.show()


#7 점그래프 scatter
figure = plt.figure()
axes = figure.add_subplot(111)
x = [1,2,3,4]
y = [2,4,6,8]
x2 = [1,1,3,4]
y2 = [6,2,4,6]
axes.scatter(x,y)
axes.scatter(x2,y2)
plt.title('제목')
plt.xlabel("엑스축 이름")
plt.ylabel("와이축 이름")
plt.show()

#8 원형 그래프
figure = plt.figure()
axes = figure.add_subplot(111)
label = ['축구', '농구', '야구', '배구']
data = [10, 20, 5, 30]
axes.pie(data, labels=label)
# plt.show()
# plt.savefig("test")