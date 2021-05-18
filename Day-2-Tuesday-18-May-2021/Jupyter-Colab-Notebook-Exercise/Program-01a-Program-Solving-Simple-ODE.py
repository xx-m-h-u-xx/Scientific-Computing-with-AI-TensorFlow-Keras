# Program 01a: A program that solves a simple ODE
from sympy import dsolve, Eq, symbols, Function
t = symbols('t')
x = symbols('x', cls = Function)
deqn1 = Eq(x(t).diff(t), 1-x(t))
sol1 = dsolve(deqn1, x(t))
print(sol1)
# Eq(x(t), C1*exp(-t) + 1)
