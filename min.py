import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def L(ro,alfa,w1,w2):
    L=((w1)/np.sin(ro))+((w2)/np.sin(np.pi-alfa-ro))
    return L

a=45
b=135
pi=np.pi
w1,w2=2,2
a*=pi/180
b*=pi/180
alfa=np.linspace(a,b,20)
ro=np.linspace(0,pi,20)

x,y=np.meshgrid(alfa,ro)
fig=plt.figure()
ax=Axes3D(fig)

ax.plot_surface(x,y,L(x,y,w1,w2))
plt.show()