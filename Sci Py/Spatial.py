import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
from scipy.spatial import KDTree
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import cosine
from scipy.spatial.distance import hamming
os.system("cls")

points =      np.array      (
                                   [
                                          [2, 4],
                                          [3, 4],
                                          [3, 0],
                                          [2, 2],
                                          [4, 1]
                                   ])
simplices = Delaunay(points).simplices
plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')
plt.show()
print()

points =      np.array      (
                                   [
                                          [2, 4],
                                          [3, 4],
                                          [3, 0],
                                          [2, 2],
                                          [4, 1]
                                   ])
a = ConvexHull(points).simplices
plt.scatter(points[:, 0], points[:, 1])
for simplex in a:
       plt.plot(points[simplex,0], points[simplex,1], 'k-')
plt.show()
print()

points =      np.array      (
                                   [
                                          [2, 4],
                                          [3, 4],
                                          [3, 0],
                                          [2, 2],
                                          [4, 1]
                                   ])
a = KDTree(points)
res = a.query((1, 1))
print(res)
print()

p1 = (1, 0)
p2 = (10, 2)
res = euclidean(p1, p2)
print(res)
print()

p1 = (1, 0)
p2 = (10, 2)
res = cityblock(p1, p2)
print(res)
print()

p1 = (1, 0)
p2 = (10, 2)
res = cosine(p1, p2)
print(res)
print()

p1 = (True, False, True)
p2 = (False, True, True)
res = hamming(p1, p2)
print(res)