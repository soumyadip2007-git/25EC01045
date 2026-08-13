import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv(r"/home/soumyadip/25EC01045/MOSFET_ID_VDS.csv")
plt.figure(1, figsize=(10,6))

for vgs,group in df.groupby("V_GS (V)"):
    plt.plot(
        group["V_DS (V)"],
        group["I_D (mA)"],
        marker = "o",
        linewidth = 2,
        label = f"$V_{{GS}}$ = {vgs} V "
    )

plt.title("MOSFET Output characteristics ($I_D$ vs $V_{DS}$)")
plt.xlabel("Drain-to-Source Voltage, $V_{DS}$(V)")
plt.ylabel("Drain Current, $I_D$(mA)")
plt.legend(title="Gate-Source Voltage")
plt.grid(True)
plt.tight_layout()
plt.savefig("id_vds.png",dpi=300)

plt.figure(2, figsize=(10,6))

for vgs,group in df.groupby("V_GS (V)"):
    vds=group["V_DS (V)"]
    id = group["I_D (mA)"]

    di_dvds=np.gradient(id,vds)

    plt.plot(
        vds,
        di_dvds,
        marker ="s",
        linestyle="--",
        linewidth=2,
        label=f"$V_{{GS}}$ = {vgs} V"
    )

plt.title("MOSFET Differential Output Conductance ($g_d = dI_D/dV_{DS}$)")
plt.xlabel("Drain-to-Source Voltage, $V_{DS}$ (V)")
plt.ylabel("Conductance, $g_ds(mS or mA/V)")
plt.legend(title="Gate-Source Voltage")
plt.grid(True)
plt.tight_layout()
plt.savefig("gd_vds.png",dpi=300)