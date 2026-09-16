# id-vds curve at vgs=0 when tox=2.9nm and 5nm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_5nm_vgs_0=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/q_10_5nm_no_qf_idvd_vgs_0.csv")
data_2_9_nm_vgs_0=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/q_10_2.93nm_no_qf_idvd_vgs_0.csv")

x=data_5nm_vgs_0["drain TotalCurrent(IdVg_n127_des) X"]
data_5nm=data_5nm_vgs_0["drain TotalCurrent(IdVg_n127_des) Y"]
data_2_9nm=data_2_9_nm_vgs_0["drain TotalCurrent(IdVg_n127_des) Y"]

plt.plot(x,data_5nm,label="$t_{ox}$ = 5 nm and $V_{GS}$ = 0V")
plt.plot(x,data_2_9nm,label="$t_{ox}$ = 2.93 nm and $V_{GS}$ = 0V")
plt.legend()
plt.xlabel("$V_{DS}$ ---->")
plt.ylabel("$I_D$ ---->")
plt.grid(True)
plt.title("Variation in $I_D$ at $t_{ox}$ = 5 and 2.93 nm ($V_{GS}$ = 0V)")
plt.show()
