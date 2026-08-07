import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print("My Roll Number is 25EC01045")
print("Python :",sys.version.split()[0])
print("numpy version is:",np.__version__)
print("pandas version :",pd.__version__)
print("matplotlib :",matplotlib.__version__)

plt.plot([0,1,2,3],[0,1,4,9],marker = "o")
plt.title("If you can see this window, the setup works")
plt.xlabel("x axis --> ")
plt.ylabel("x squared or y axis")
plt.show()