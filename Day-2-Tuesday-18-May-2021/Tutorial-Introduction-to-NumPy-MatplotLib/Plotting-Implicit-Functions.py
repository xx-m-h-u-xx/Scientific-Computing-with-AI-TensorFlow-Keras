''' Plotting implicit functions '''
# ''' equation of elipse '''


x , y = np.mgrid[-5:5:100j, -5:5:100j]          # a grid of x,y values
z = x**2 / 4 + y**2                             # a function of two variables
plt.contour (x,y,z,levels=[1])                  # The curve x**2/4+y**2=1



''' A parameter plot '''

t = np.linspace(0, np.pi, 100)          # set of t values
x = 0.7*np.sin(t+1)*np.sin(3*t)         # set of x values
y = 0.7*np.cos(t+1)*np.sin(3*t)         # set of y values

# 2D parametric plot
plt.plot(x,y)
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.title('Parametric Plot')
