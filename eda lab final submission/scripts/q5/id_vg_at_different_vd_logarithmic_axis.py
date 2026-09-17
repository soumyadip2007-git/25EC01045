import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/q5_idvg.csv")

x=data["Vd_0.05 X"]
data_1=data["Vd_0.05 Y"]
data_2=data["Vd_0.4 Y"]

mask=((x>0.5)&(x<0.6))
coeff1=np.polyfit(x[mask],(np.log10(data_1[mask])),1)
coeff2=np.polyfit(x[mask],np.log10(data_2[mask]),1)

plt.figure(figsize=(10,6))
plt.semilogy(x,data_1,label="$V_{DS}$ = 0.05 V")
plt.semilogy(x,data_2,label="$V_{DS}$ = 0.4 V")
plt.xlabel("$V_{GS}$ ---->")
plt.ylabel("$I_D$ ---->")
plt.grid(True)
plt.title("$I_D$-$V_{GS}$ curve at different $V_{DS}$ in Logarithmic axis")
plt.text(1,1e-5,f"Sub-threshold slope at $V_{{DS}}$ = 0.05 V is {1/coeff1[0]*1000} mV/dec",fontsize=12)
plt.text(1,1e-6,f"Sub-threshold slope at $V_{{DS}}$ = 0.4 V is {1/coeff2[0]*1000} mV/dec",fontsize=12)
plt.legend()
plt.show()
