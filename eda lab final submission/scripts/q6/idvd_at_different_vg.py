import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/Q6_id_vd_at_const_vgs.csv")
x=data["vgs_0.3 X"]
vgs_3=data["vgs_0.3 Y"]
vgs_6=data["vgs_0.6 Y"]
vgs_9=data["vgs_0.9 Y"]
vgs_15=data["vgs_1.5 Y"]
plt.plot(x,vgs_3,label="$V_{GS}$ = 0.3 V")
plt.plot(x,vgs_6,label="$V_{GS}$ = 0.6 V")
plt.plot(x,vgs_9,label="$V_{GS}$ = 0.9 V")
plt.plot(x,vgs_15,label="$V_{GS}$ = 1.5 V")
plt.xlabel("$V_{DS}$ ---->")
plt.ylabel("$I_D$ ---->")
plt.title("$I_D$-$V_{DS}$ curve at Constant $V_{GS}$")
plt.grid(True)
plt.legend(loc="best")
plt.show()
