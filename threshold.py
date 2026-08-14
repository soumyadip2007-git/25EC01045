import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r"/home/soumyadip/25EC01045/MOSFET_ID_VGS.csv")
vds_df=df[np.isclose(df["V_DS (V)"],1.0)].copy()
vgs = vds_df["V_GS (V)"].values
id = vds_df["I_D (mA)"].values

gm = np.gradient(id,vgs)
peak_idx=np.argmax(gm)

vgs_win=vgs[peak_idx-2:peak_idx+1]
id_win=id[peak_idx-2:peak_idx+1]

m,c=np.polyfit(vgs_win,id_win,1)

vt = -c/m
print("Threshold voltage = ",vt)
print("Threshold voltage = ",vt)
print(f"peak gm is {gm[peak_idx]} and corresponding vgs is {peak_idx}")
