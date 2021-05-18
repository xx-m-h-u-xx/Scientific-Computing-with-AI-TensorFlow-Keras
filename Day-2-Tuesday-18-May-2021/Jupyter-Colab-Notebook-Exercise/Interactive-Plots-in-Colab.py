# interactive plot
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

def f(A, B, C, D):
  plt.figure(2)
  x = np.linspace(-10, 10, num =1000)
  plt.plot(x, A * np.sin(B * (x + C)) + D)
  plt.ylim(-5, 5)
interactive_plot = interactive(f, A=(0,2),B = (0,2 * np.pi), C = (0,2 * np.pi), 
                                  D = (-3, 3, 0.5))
output = interactive_plot.children[-1]
output.layout.height = '350px'
interactive_plot
