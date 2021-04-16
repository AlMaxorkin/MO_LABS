import numpy as np
import sympy as sp

a0 = 0
a1 = 0
a2 = 1
a3 = 1
a4 = -2
a5 = 1


def J(u):
    return a0*(u**5) + a1*(u**4) + a2*(u**3) + a3*(u**2) + a4*u + a5


def dJ(u):
    return 5*a0*(u**4) + 4*a1*(u**3) + 3*a2*(u**2) + 2*a3*u + a4


def ddJ(u):
    return 20*a0*(u**3) + 12*a1*(u**2) + 6*a2*u + 2*a3


eps = 0.0004
uk = 10
k = 0
while abs(dJ(uk)) > eps:
    k+=1
    uk -= dJ(uk)/ddJ(uk)


print(k)
print("u_min =", uk)
print("J(u_min) =", J(uk))