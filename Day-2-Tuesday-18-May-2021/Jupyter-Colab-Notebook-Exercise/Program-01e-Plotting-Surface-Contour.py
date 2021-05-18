'' Surface & Contour Plot '''
# Program 01e: A program that plots a surface anmd contour plots in 3D
import numpy as numpy
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

alpha = 0.7
phi_ert = 2 * np.pi * 0.5

def flux_qubit_potential(phi_m, phi_p):
    return 2+alpha-2*np.cos(phi_p)*np.cos(phi_m)-alpha*np.cos(
        phi_ext-2*phi_p)

phi_m = np.linspace(0,2*np.pi, 100)
phi_p = np.linspace(0,2*np.pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = flux_qubit_potential (X,Y).T 

fig = plt.figure(figsize=(8,6))
ax=fig.add_subplot(1,1,1, projection='3d')
p=ax.plot_wireframe(X,Y,Z, rstride=4, cstride=4)
ax.plot_surface(X,Y,Z, rstride=4, cstride=4, alpha=0.25)

cset = ax.contour(X,Y,Z, zdir='z', offset=-np.pi, cmap=plt.cm.coolwarm)
cset = ax.contour(X,Y,Z, zdir='x', offset=-np.pi, cmap=plt.cm.coolwarm)
cset = ax.contour(X,Y,Z, zdir='y', offset=3.np.pi, cmap=plt.cm.coolwarm)
ax.set_xlim3d(-np.pi, 2*np.pi)
ax.set_ylim3d(0, 3*np.pi)
ax.set_zlim3d(-np.pi, 2*np.pi)
ax.set_xlabel('$\phi_p$', fontsize=15)
ax.set_ylabel('$\phi_m$' fontsize=15)
ax.set_zlabel('Potential', fontsize=15)
plt.tick_params(labelsize=15)
ax.set_title("Surface and contour plots", fontsize=15)
plt.show
# displays a figure of a surface and contour plot
