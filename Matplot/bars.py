import os
import numpy as np
import matplotlib.pyplot as plt
os.system("cls")

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([8, 9, 10, 11, 12])
# plt.bar(x, y)
# plt.show()
# print()

# x = np.array(["A", "B", "C", "D", "E"])
# y = np.array([8, 9, 10, 11, 12])
# plt.bar(x, y)
# plt.show()
# print()

# x = ["Munna", "Radha"]
# y = [143, 225]
# plt.bar(x, y)
# plt.show()
# print()

# x = ["Munna", "Radha"]
# y = [143, 225]
# plt.barh(x, y)
# plt.show()
# print()

# x = ["Munna", "Radha"]
# y = [143, 225]
# plt.bar(x, y, color = "green")
# plt.show()
# print()

# x = ["Munna", "Radha"]
# y = [143, 225]
# plt.bar(x, y, color = "#0ff")
# plt.show()
# print()

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([8, 9, 10, 11, 12])
# plt.bar(x, y, color = "#0ff", width = 0.1)     # default 0.8
# plt.show()
# print()

x = np.array([1, 2, 3, 4, 5])
y = np.array([8, 9, 10, 11, 12])
plt.barh(x, y, color = "#0ff", height = 0.1)     # default 0.8
plt.show()