import random
import time
import numpy as np
import sympy as sp

a0 = 0
a1 = 0
a2 = 1
a3 = 1
a4 = -2
a5 = 1
u = sp.symbols('u')


def J(u):
    return a0 * (u ** 5) + a1 * (u ** 4) + a2 * (u ** 3) + a3 * (u ** 2) + a4 * u + a5


def dJ(u):
    return 5 * a0 * (u ** 4) + 4 * a1 * (u ** 3) + 3 * a2 * (u ** 2) + 2 * a3 * u + a4


N = 20
u0 = 0
alpha = 0.1
eps = 0.0005

while abs(dJ(u0)) >= eps:
    u1 = u0 - alpha * dJ(u0)
    while J(u1) > J(u0):
        u1 = u0 - alpha * dJ(u0)
        alpha /= 2
    u0 = u1

print(u0)
print(J(u0))
