# idvgs at vds=0.4 and tox = 5, 3.4 nm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/q_10_5nm_no_qf_idvg_vds_0.4.csv")
data1=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/q_10_3.5_nm_no_qf_idvg_vds_0.4.csv")

x=data["drain TotalCurrent(IdVg_n128_des) X"]
data_1=data["drain TotalCurrent(IdVg_n128_des) Y"]
data_2=data1["drain TotalCurrent(IdVg_n128_des) Y"]

line1,=plt.plot(x,data_1,label="$t_{ox}$ = 5nm and $V_{DS}$ = 0.4V")
line2,=plt.plot(x,data_2,label="$t_{ox}$ = 3.5nm and $V_{DS}$ = 0.4V")

win=0.1
mask=(x>(1-win)) & (x<(1+win))
mask1=x<1.25
x2=x[mask1]

# x1=x[mask]
# xplot1,yplot1=line1.get_data()
# xplot2,yplot2=line2.get_data()

# idx1=np.where(xplot1==x1)[0][0]
# idx2=np.where(xplot2==x1)[0][0]

# value1=yplot1[idx1]
# value2=yplot2[idx2]

coeff1=np.polyfit(x[mask],data_1[mask],1)
coeff2=np.polyfit(x[mask],data_2[mask],1)

t1=np.poly1d(coeff1)
t2=np.poly1d(coeff2)

line3,=plt.plot(x[mask1],t1(x2),label="Tangent when $t_{ox}$ = 5nm")
line4,=plt.plot(x[mask1],t2(x2),label="Tangent when $t_{ox}$ = 3.5nm",color="black")

plt.legend(loc="lower right")
plt.grid(True)
plt.title("$I_D$-$V_{GS}$ curve at $t_{ox}$ = 5, 3.5 nm with $V_{DS}$ = 0.4V")
plt.xlabel("$V_{GS}$ ---->")
plt.ylabel("$I_D$ ---->")
plt.text(0,0.0006,f"Threshold voltage when $t_{{ox}}$=5nm and $V_{{DS}}$=0.4V is {-coeff1[1]/coeff1[0]} V",fontsize=12)
plt.text(0,0.0005,f"Threshold voltage when $t_{{ox}}$=3.5nm and $V_{{DS}}$=0.4V is {-coeff2[1]/coeff2[0]} V",fontsize=12)
plt.show()

