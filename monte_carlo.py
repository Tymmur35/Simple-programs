import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

def rocurve(T0, T1,ngam):
    gammin = np.min([np.min(T0),np.min(T1)])
    gammax = np.max([np.max(T0),np.max(T1)])
    gam=np.linspace(gammin,gammax,ngam)
    Pfa=np.zeros(ngam)
    Pd=np.zeros(ngam)
    for zyzz in range(ngam):
        v0=T0>gam[zyzz]
        v1=T1>gam[zyzz]
        Pfa[zyzz]=np.sum(v0)/len(T0)
        Pd[zyzz]=np.sum(v1)/len(T1)
    return Pfa,Pd

number_of_simulations=10000
x_H0=np.zeros(number_of_simulations)
x_H1=np.zeros(number_of_simulations)

for i in range(number_of_simulations):
    x_H0[i]=np.sum(np.square(np.random.normal(0,2,100)))
    x_H1[i]=np.sum(np.square(np.random.normal(1,2,100)))

(Pfa,Pd)=rocurve(x_H0, x_H1,1000)


plt.plot(Pfa, Pd, 'b' ,label='Energy Detector')
plt.grid()
plt.legend()
plt.ylabel('$P_D$')
plt.xlabel('$P_{FA}$')
# ax = plt.axes()
# ax.xaxis.set_ticks_position('none') 
# ax.yaxis.set_ticks_position('none') 
axes1 = plt.gca()
axes1.set_xlim([0.01,1])
axes1.set_ylim([0.01,1])
#plt.legend(loc='upper right',bbox_to_anchor=(0.95, 1), ncol=1, fancybox=False, shadow=False)
plt.legend(loc = 'best')
plt.xscale("log")
plt.yscale("log")
plt.show()


