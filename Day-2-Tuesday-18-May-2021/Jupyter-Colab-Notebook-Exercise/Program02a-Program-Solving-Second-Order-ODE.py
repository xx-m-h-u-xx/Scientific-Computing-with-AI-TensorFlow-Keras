# Program 02a: A program that solves a second order ODE
from sympy import dsolve, Eq, symbols, Function, ex
t = symbols('t')
y = symbols('y', cls = Function)
deqn2 = Eq(y(t).diff(t,t)+y(t).diff(t)+y(t), exp(t))
sol2 = dsolve(deqn2, y(t))
print(sol2)

# prints out:
# Eq(y(t), (C1*sin(sqrt(3)*t/2) + C2*cos(sqrt(3)*t/2))/sqrt(exp(t)) + exp(t)/3)
