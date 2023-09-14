import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [4,5,2,7]
x1 = [1,5,3,4]
y1 = [4,5,8,7]
x2 = [1,2,3,1]
y2 = [4,1,2,7]
x3 = [1,2,3,4]
y3 = [3,3,2,7]

x4 = np.array(x)
y4 = np.array(y)
x5 = np.array(x2)
y5 = np.array(y2)
x6 = np.array(x3)
y6 = np.array(y3)
x7 = np.array(x1)
y7 = np.array(y1)

figure = plt.figure()
axes1 = figure.add_subplot(221)
axes2 = figure.add_subplot(222)
axes3 = figure.add_subplot(223)
axes4 = figure.add_subplot(224)
axes1.plot(x4, y4)
axes2.plot(x5, y5)
axes3.plot(x6, y6)
axes4.plot(x7, y7)

plt.show()



