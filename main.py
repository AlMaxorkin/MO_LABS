import random

import numpy as np

a0 = 0
a1 = 0
a2 = 0
a3 = 1
a4 = 1
a5 = 1


def J(u):
    return a0*(u**5) + a1*(u**4) + a2*(u**3) + a3*(u**2) + a4*u + a5


def division(a, b, J, epsilon):
    while abs(b-a) >= epsilon:
        n = 0
        delta = random.uniform(0, (b-a)/2)
        u1 = (b + a - delta) / 2
        u2 = (b + a + delta) / 2

        J1 = J(u1)
        J2 = J(u2)

        if J1 > J2:
            a = u1
        elif J1 < J2:
            b = u1
        else:
            b = u2
            a = u1
        n += 1

    return (b + a) / 2


def golden_ratio(a, b, J, epsilon):
    n = 0
    alpha1 = (3 - np.sqrt(5)) / 2
    alpha2 = (np.sqrt(5) - 1) / 2

    u1 = a + alpha1 * (b - a)
    u2 = a + alpha2 * (b - a)

    while abs(b-a) >= epsilon:
        n += 1

        J1 = J(u1)
        J2 = J(u2)
        if J1 < J2:
            b = u2
            u2 = u1
            u1 = a + alpha1 * (b - a)
        elif J1 > J2:
            a = u1
            u1 = u2
            u2 = a + alpha2 * (b - a)
        else:
            b = u2
            a = u1
            u1 = a + alpha1 * (b - a)
            u2 = a + alpha2 * (b - a)

    return (b + a) / 2


print(division(-2, 2, J, epsilon=10**(-4)))
print(golden_ratio(-2, 2, J, epsilon=10**(-4)))

