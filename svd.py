import numpy as np

A = np.array([[1, 2], [3, 4]])

u, s, vT = np.linalg.svd(A)

sigma = np.zeros((A.shape[0], A.shape[1]))
np.fill_diagonal(sigma, s)

B = u.dot(sigma.dot(vT))
print("Original matrix A:")
print(A)

print("\nMatrix U:")
print(u)

print("\nSingular values (s):")
print(s)

print("\nMatrix Sigma :")
print(sigma)

print("\nMatrix V^T:")
print(vT)

print("\nReconstructed matrix B:")
print(B)

'''
output

Original matrix A:
[[1 2]
 [3 4]]

 Reconstructed matrix B:
[[1. 2.]
 [3. 4.]]
mlm@mlm-desktop:~$ python3 svd.py
Original matrix A:
[[1 2]
 [3 4]]

Matrix U:
[[-0.40455358 -0.9145143 ]
 [-0.9145143   0.40455358]]

Singular values (s):
[5.4649857  0.36596619]

Matrix Sigma (Σ):
[[5.4649857  0.        ]
 [0.         0.36596619]]

Matrix V^T:
[[-0.57604844 -0.81741556]
 [ 0.81741556 -0.57604844]]

Reconstructed matrix B:
[[1. 2.]
 [3. 4.]]
'''


