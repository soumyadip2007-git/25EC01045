import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/Q6_id_vd_at_const_vgs.csv")
x=data["vgs_0.3 X"]
vgs_15=data["vgs_1.5 Y"]
gd=np.gradient(vgs_15,x)
line,=plt.plot(x,gd)
plt.grid(True)
plt.xlabel("$V_{DS}$ ---->")
plt.ylabel("$g_D$ ---->")
plt.title("Value of $g_D$ at constant $V_{GS}$ = 1.5 V")


# 1. Extract data from the plot
x_plot, y_plot = line.get_data()

# 2. Define an arbitrary x value
target_x = 2.9 

# 3. Use numpy's linear interpolation to estimate the y-value
target_y = np.interp(target_x, x_plot, y_plot)
plt.show()
print(target_y)
print("The resistance at saturation at V_gs = 1.5V is",1/(target_y*1000),"kiloohm/micrometer")
