from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0,1,1000)
fm = 2; fc = 300; Vm = 10; Vc = 20
mt = Vm*np.cos(2*np.pi*fm*t)
# ct = Vc*np.cos(2*np.pi*fc*t)
DSBSC = (Vc+mt)*np.cos(2*np.pi*fc*t)
# Plot the data
plt.subplot(1,2,1)
plt.plot(t, DSBSC, 'b' ,label='AM Signal')
plt.grid()
# Add a legend
plt.legend()
plt.ylabel('Voltage')
plt.xlabel('Time')
axes1 = plt.gca()
axes1.set_xlim([0,1])
axes1.set_ylim([-30,30])
plt.legend(loc='upper right',bbox_to_anchor=(0.95, 1), ncol=1, fancybox=False, shadow=False)
#plt.legend(loc = 'best')

plt.subplot(1,2,2)
plt.plot(t, mt, 'k', label='Message Signal')

plt.grid()
# Add a legend
plt.legend()
plt.ylabel('Voltage')
plt.xlabel('Time')
axes = plt.gca()
axes.set_xlim([0,1])
axes.set_ylim([-10,10])
plt.legend(loc='upper right',bbox_to_anchor=(0.95, 1), ncol=1, fancybox=False, shadow=False)
#plt.legend(loc = 'best')
plt.tight_layout()
plt.show()