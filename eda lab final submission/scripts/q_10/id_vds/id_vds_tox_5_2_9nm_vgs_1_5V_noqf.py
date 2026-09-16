# id-vds curve at vgs= 1.5 V when tox=2.9nm and 5nm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_5nm_vgs_1_5=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/q_10_5nm_no_qf_idvd_vgs_1.5.csv")
data_2_9_nm_vgs_1_5=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/q_10_2.93nm_no_qf_idvd_vgs_1.5.csv")

x=data_5nm_vgs_1_5["drain TotalCurrent(IdVg_n127_des) X"]
data_5nm=data_5nm_vgs_1_5["drain TotalCurrent(IdVg_n127_des) Y"]
data_2_9nm=data_2_9_nm_vgs_1_5["drain TotalCurrent(IdVg_n127_des) Y"]

plt.plot(x,data_5nm,label="$t_{ox}$ = 5 nm and $V_{GS}$ = 1.5V")
plt.plot(x,data_2_9nm,label="$t_{ox}$ = 2.93 nm and $V_{GS}$ = 1.5V")
plt.legend()
plt.xlabel("$V_{DS}$ ---->")
plt.ylabel("$I_D$ ---->")
plt.grid(True)
plt.title("Variation in $I_D$ at $t_{ox}$ = 5 and 2.93 nm ($V_{GS}$ = 1.5V) and no $Q_f$")
plt.show()