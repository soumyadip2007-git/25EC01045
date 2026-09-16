import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/q_2_vertical_cutline_new.csv")
x=data["DopingConcentration_vertical X"]
y=data["DopingConcentration_vertical Y"]
xtick=np.arange(0,0.65,0.05)
plt.figure(figsize=(10,6))
plt.plot(x,y)
plt.xlabel("x ---->")
plt.ylabel("Doping Concentration")
plt.xticks(xtick)
plt.title("Doping Concentration Along Vertical Cutline")
plt.grid(True)
plt.show()