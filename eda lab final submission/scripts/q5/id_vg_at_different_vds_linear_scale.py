import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv(r"/mnt/c/Users/soumy/OneDrive/Desktop/eda lab data/25EC01045_Lab_data_final/25EC01045/made_document/q5_idvg.csv")

x=data["Vd_0.05 X"]
data_1=data["Vd_0.05 Y"]
data_2=data["Vd_0.4 Y"]

mask=(x<0.75) & (x>0.5)
coeff1=np.polyfit(x[mask],data_1[mask],1)
coeff2=np.polyfit(x[mask],data_2[mask],1)

t1=np.poly1d(coeff1)
t2=np.poly1d(coeff2)

mask1=(x<1.25)
x1=x[mask1]

plt.figure(figsize=(10,6))
plt.plot(x,data_1,label="$V_{DS}$ = 0.05 V")
plt.plot(x,data_2,label="$V_{DS}$ = 0.4 V")

plt.plot(x[mask1],t1(x1),label="Tangent when $V_{DS}$ = 0.05 V")
plt.plot(x[mask1],t2(x1),label="Tangent when $V_{DS}$ = 0.4 V",color="black")

plt.xlabel("$V_{GS}$ ---->")
plt.ylabel("$I_D$ ---->")
plt.grid(True)
plt.title("$I_D$-$V_{GS}$ curve at different $V_{DS}$ in Linear Scale")
plt.legend(loc="lower right")
plt.text(0,0.0006,f"The Threshold Voltage at $V_{{DS}}$ = 0.05 V is {-coeff1[1]/coeff1[0]}",fontsize=10)
plt.text(0,0.0005,f"The Threshold Voltage at $V_{{DS}}$ = 0.4 V is {-coeff2[1]/coeff2[0]}",fontsize=10)
plt.show()
