import numpy as np
ar1=np.array([[2,4],[8,9]])
ar2=np.array([[5,6],[7,8]])

print("matrix addiction:")
print(np.add(ar1,ar2))

print("matrix subtraction:")
print(np.subtract(ar1,ar2))

print("matrix multiplication:")
print(np.multiply(ar1,ar2))

print("matrix division:")
print(np.divide(ar1,ar2))

print("matrix multi:")
print(np.dot(ar1,ar2))

print("matrix diagonal:")
print(np.trace(ar1))

print("matrix transpose:")
print(ar1.transpose())                

'''
OUTPUT

matrix addiction:
[[ 7 10]
 [15 17]]
matrix subtraction:
[[-3 -2]
 [ 1  1]]
matrix multiplication:
[[10 24]
 [56 72]]
matrix division:
[[0.4        0.66666667]
 [1.14285714 1.125     ]]
matrix multi:
[[ 38  44]
 [103 120]]
matrix diagonal:
11
matrix transpose:
[[2 8]
 [4 9]]
'''


