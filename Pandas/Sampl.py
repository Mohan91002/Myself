import os
import pandas as pd
os.system("cls")

dataset =     {
                     'cars'        :      ["BMW", "Volvo", "Ford"],
                     'passings'    :      [3, 7, 2]
              }
var = pd.DataFrame(dataset)
print(var)
print()

print(pd.__version__)
print()