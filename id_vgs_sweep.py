import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv(r"/home/soumyadip/25EC01045/MOSFET_ID_VGS.csv")

fig,ax = plt.subplots(1,2,figsize=(11, 4.2))
for vds,group in df.groupby("V_DS (V)"):

    group = group.sort_values("V_GS (V)")
    gm = np.gradient(group["I_D (mA)"], group["V_GS (V)"])
    ax[0].plot(group["V_GS (V)"],group["I_D (mA)"],
            label=f"$V_{{DS}}$ = {vds}"
               )
    ax[1].plot(group["V_GS (V)"],gm,
                label=f"$V_{{DS}}$ = {vds}"
                   )

ax[0].set_title("Transfer Characteristics")
ax[0].set_xlabel("$V_{GS}$ (V)")
ax[0].set_ylabel("$I_D$ (mA)")
ax[1].set_title("Transconductance $g_m = dI_D/dV_{GS}$")
ax[1].set_xlabel("$V_{GS}$ (V)")
ax[1].set_ylabel("$g_m$ (mS)")

for a in ax:
    a.grid(True)
    a.legend(fontsize=9)

plt.tight_layout()
plt.savefig("gm_tarnsfer.png", dpi=300)
plt.show()