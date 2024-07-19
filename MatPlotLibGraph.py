import numpy as np
import matplotlib.pyplot as plt
import time

x = []
y = []

for i in range(1, 100):
    x.append(i)
    y.append(i * i)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Line Plot')
plt.show()

# y = np.array([0.01, 0.02, 0.03, 0.04])
# #
# x = np.array([0.01127, 0.021952, 0.031752, 0.042924])
# f = []
# for i in y:
#   f.append(np.log(i))
# print(y.tolist())

# print(f)
# coefficients = np.polyfit(x, y, 1)
# print(coefficients)
# line_function = np.poly1d(coefficients)

# slope = coefficients[0]
# print("Slope:", slope)

# lrl = line_function(x)
# plt.style.use('dark_background')
# plt.scatter(x, y)
# plt.plot(x,lrl,color="red")
# plt.grid()
# plt.show()
# j = np.array([])
# for i in range(len(y)):
#   sq = (y[i]-lrl[i])**2
#   j = np.append(j,sq)
# print(np.sum(j)/(2*len(y)))