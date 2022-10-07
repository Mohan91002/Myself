import os
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order
os.system("cls")

a = np.array  (
              [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
              )
b = csr_matrix(a)
print(connected_components(b))
print()

a = np.array  (
              [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
              )
b = csr_matrix(a)
print(dijkstra(b))
print()

a = np.array  (
              [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
              )
b = csr_matrix(a)
print(dijkstra(b, return_predecessors = True, indices = 0))
print()

a = np.array  (
              [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
              )
b = csr_matrix(a)
print(floyd_warshall(b, return_predecessors = True))
print()

a = np.array  (
              [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
              )
b = csr_matrix(a)
print(bellman_ford(b, return_predecessors = True, indices = 0))
print()

a = np.array  (
              [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
              )
b = csr_matrix(a)
print(depth_first_order(b, 1))
print()

a = np.array  (
              [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
              )
b = csr_matrix(a)
print(breadth_first_order(b, 1))