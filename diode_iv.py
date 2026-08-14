import numpy as np
import matplotlib.pyplot as plt

i_s=10**(-12)
n=[1.0,1.5,2.0]
v_d = np.arange(0,0.81,0.01)
v_t=0.02585
x=1


for i in n:
    def f(v_d):
        return i_s*(np.exp(v_d/(i*v_t)))
    i_d=f(v_d)
    plt.subplot(1,2,1)
    plt.semilogy(v_d,i_d,label=f"Diode Characteristics with ideality factor {i}")
    plt.xlabel("$V_D$")
    plt.ylabel("$I_D$")
    plt.legend()
    plt.grid(True)
    x+=1
for i in n:
    def f(v_d):
        return i_s*(np.exp(v_d/(i*v_t)))
    i_d=f(v_d)
    plt.subplot(1,2,2)
    g_d = np.gradient(i_d,v_d)
    plt.semilogy(g_d,i_d,label=f"Diode Conductance with ideality factor {i}")
    plt.xlabel("$g_D$")
    plt.ylabel("$I_D$")
    plt.legend()
    plt.grid(True)
    x+=1
plt.show()
