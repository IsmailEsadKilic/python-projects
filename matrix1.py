import numpy as np


matrixRight = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
matrixLeft = [[0, -2, 2], [5, 1, 5], [1, 4, -1]]


# result = np.dot(matrixLeft, matrixRight)
# result = np.matmul(matrixLeft, matrixRight)
result = matrixLeft @ matrixRight
print(result)

matrix1 = np.array([[8, 4], [6, 10]])
result1 = np.linalg.det(matrix1)
print(result1)

result2 = np.linalg.inv(matrix1)
print(result2)

result3 = np.linalg.eigvals(matrix1)
print(result3)

result4 = np.linalg.eig(matrix1)
print(result4)