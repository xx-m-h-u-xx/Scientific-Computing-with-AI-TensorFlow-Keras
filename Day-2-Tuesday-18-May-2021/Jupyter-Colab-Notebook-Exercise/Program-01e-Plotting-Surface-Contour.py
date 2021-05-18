''' Surface & Contour Plot '''
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
