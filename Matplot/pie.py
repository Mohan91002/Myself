import os
import numpy as np
import matplotlib.pyplot as plt
os.system("cls")

# x = np.array([10, 25, 25, 10, 25, 5])
# plt.pie(x)
# plt.show()
# print()

# x = np.array([35, 25, 25, 15])
# l = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(x, labels = l)
# plt.show()
# print()

# x = np.array([35, 25, 25, 15])
# l = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(x, labels=l, startangle=90)
# plt.show()
# print()

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]
# plt.pie(y, labels=mylabels, explode=myexplode)
# plt.show()
# print()

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]
# plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
# plt.show()
# print()

# y = np.array([35, 25, 25, 15])
# l = ["Apples", "Bananas", "Cherries", "Dates"]
# o = ["#00ffff", "#ff00ff", "#ffff00", "#ffffff"]
# e = [0.2, 0.2, 0.2, 0.2]
# plt.pie(y, labels = l, explode = e, shadow = True, colors = o)
# plt.show()
# print()

# y = np.array([35, 25, 25, 15])
# l = ["Apples", "Bananas", "Cherries", "Dates"]
# o = ["#00ffff", "#ff00ff", "#ffff00", "#000"]
# e = [0.2, 0.2, 0.2, 0.2]
# plt.pie(y, labels=l, colors=o, explode=e, shadow=True)
# plt.legend()
# plt.show()
# print()

y = np.array([35, 25, 25, 15])
l = ["Apples", "Bananas", "Cherries", "Dates"]
o = ["#00ffff", "#ff00ff", "#ffff00", "#000"]
e = [0.2, 0.2, 0.2, 0.2]
plt.pie(y, labels=l, colors=o, explode=e, shadow=True)
plt.legend(title= "munna")
plt.show()