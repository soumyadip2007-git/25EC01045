import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
df = pd.read_csv(r"/home/soumyadip/25EC01045/Diode_IV_Temperature.csv")
for temp,group in df.groupby("T (C)"):
    plt.plot(
            group["V (V)"],
            group["I (mA)"],
            marker = "o",
            linewidth = 2,
            label = f"T (C) = {temp}",
    )
plt.title("Diode I_V characteristics at different temperature")
plt.xlabel("Temperature")
plt.ylabel("I (mA)")
plt.legend(title="$I_{D}$-$V_{D}$ character of Diode")
plt.grid(True)
plt.tight_layout()
plt.savefig("/home/soumyadip/25EC01045/id_vd_of_diode.png",dpi=350)
plt.show()