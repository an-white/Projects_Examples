import pandas as pd, numpy as np, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

## with the function defined find the integers values that belong to the function and show a graph ##

def Fz(X,Y):
    return (6500-(18*(X)**3+11*(Y)**5))**(1/6)

Vx,Vy,Vz=[],[],[]
k,cx,cy,cz=0,0,0,0
lim=6500
x,y,z=0,0,0
cont=0
signal=True

while signal==True:
    k=k+1
    E1=18*k**3
    E2=11*k**5 
    E3=8*k**6

    if E1<lim:
        cx=cx+1

    if E2<lim:
        cy=cy+1

    if E3<lim:
        cz=cz+1

    if E1>lim and E2>lim and E3>lim:
            ran=cx
            if cy>ran:
                ran=cy
            if cz>ran:
                ran=cz
            for x in range(ran):
                for y in range(ran):
                    for z in range(ran): 
                        E1=18*(x+1)**3
                        E2=11*(y+1)**5 
                        E3=8*(z+1)**6
                        E=E1+E2+E3
                        cont=cont+1
                        if E<6500:
                            Vx.append(x+1)
                            Vy.append(y+1)
                            Vz.append(z+1)
            signal=False

            # def entry values
            X,Y=np.meshgrid(Vx,Vy)
            fig=plt.figure()
            ax=Axes3D(fig)
            # def values of z to plot the mesh
            ax.plot_surface(X,Y,Fz(X,Y))
            plt.show()

            # def entry values
            X,Y=np.meshgrid(Vx,Vy)
            fig=plt.figure()
            ax=Axes3D(fig)
            # PLOT of the contours of the mesh
            ax.contour(X,Y,Fz(X,Y))
            plt.show()
            
            # def entry values
            X,Y=np.meshgrid(Vx,Vy)
            fig=plt.figure()
            ax=Axes3D(fig)
            # PLOT of the GRADIENT with colors 
            ax.contourf(X,Y,Fz(X,Y))
            plt.show()