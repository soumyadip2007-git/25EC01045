import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data1=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/q_10_5nm_no_qf_idvd_vgs_1.5.csv")
data2=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/q_10_5nm_with_qf_idvd_vgs_1.5.csv")
x=data1["drain TotalCurrent(IdVg_n127_des) X"]
no_qf=data1["drain TotalCurrent(IdVg_n127_des) Y"]
with_qf=data2["drain TotalCurrent(IdVg_n127_des) Y"]

plt.plot(x,no_qf,label="Without $Q_f$ and $V_{GS}$ = 1.5V")
plt.plot(x,with_qf,label="With $Q_f$ and $V_{GS}$ = 1.5V")
plt.legend()
plt.xlabel("$V_{DS}$ ---->")
plt.ylabel("$I_D$ ---->")
plt.grid(True)
plt.title("Variation in $I_D$ with and without $Q_f$ ($V_{GS}$ = 1.5V) and $t_{ox}$=5nm")
plt.show()