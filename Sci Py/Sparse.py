import os
import numpy as np
from scipy.sparse import csr_matrix
os.system("cls")

a = np.array([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7])
print(csr_matrix(a))
print()

a = np.array([[0, 1, 0], [2, 0, 3], [0, 4, 0], [5, 0, 6]])
print(csr_matrix(a))
print()

a = np.array([[0, 1, 0], [2, 0, 3], [0, 4, 0], [5, 0, 6]])
print(csr_matrix(a).data)
print()

a = np.array([[0, 1, 0], [2, 0, 3], [0, 4, 0], [5, 0, 6]])
print(csr_matrix(a).count_nonzero())
print()

a = np.array([[0, 1, 0], [2, 0, 3], [0, 4, 0], [5, 0, 6]])
mat = csr_matrix(a)
mat.eliminate_zeros()
print(mat)
print()

a = np.array([[0, 1, 0], [2, 2, 3], [0, 4, 4], [5, 6, 6]])
mat = csr_matrix(a)
mat.sum_duplicates()
print(mat)
print()

a = np.array([[0, 1, 0], [2, 2, 3], [0, 4, 4], [5, 6, 6]])
mat = csr_matrix(a).tocsc()
print(mat)