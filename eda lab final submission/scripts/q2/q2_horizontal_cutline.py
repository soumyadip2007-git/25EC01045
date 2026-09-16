import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/q_2_horizontal_cutline_new.csv")
x=data["DopingConcentration_horizontal X"]
y=data["DopingConcentration_horizontal Y"]
plt.figure(figsize=(10,6))
plt.plot(x,y)
plt.xlabel("x ---->")
plt.ylabel("Doping Concentration")
plt.title("Doping Concentration Along Horizontal Cutline")
plt.grid(True)
plt.show()