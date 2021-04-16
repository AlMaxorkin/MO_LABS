import numpy as np
import random

a0 = 0
a1 = 0
a2 = 1
a3 = 1
a4 = -2
a5 = 1


def J(u):
    return a0*(u**5) + a1*(u**4) + a2*(u**3) + a3*(u**2) + a4*u + a5


a = 0
b = 1
eps = 0.0001
delta = random.uniform(a, b)
u1 = random.uniform(a, a + delta)
u2 = random.uniform(a, b)
u3 = random.uniform(b - delta, b)

d1 = J(u1) - J(u2)
d2 = J(u3) - J(u2)

while True:
    if (d1 >= 0) and (d2 >= 0) and (d1 + d2 > 0):
        break
    u2 = random.uniform(u1, u3)
    d1 = J(u1) - J(u2)
    d2 = J(u3) - J(u2)


w = u2 + (((u3 - u2)**2)*d1 - ((u2 - u1)**2)*d2)/(2*((u3 - u2)*d1 - (u2 - u1)*d2))

if w < u2:
    if J(w) < J(u2):
        u3 = u2
        u2 = w
    elif J(w) > J(u2):
        u1 = w
    else:
        if J(u1) > J(u2):
            u3 = u2
            u2 = w
        elif J(u2) > J(u3):
            u1 = w
elif w > u2:
    if J(w) < J(u2):
        u1 = u2
        u2 = w
    elif J(w) > J(u2):
        u3 = w
    else:
        if J(u3) > J(u2):
            u1 = u2
            u2 = w
        elif J(u1) > J(u2):
            u3 = w

delta = random.uniform(0, (u3 + u1) / 2)

n = 0
while delta > eps:
    n += 1
    if J(u2 + delta) < J(u2):
        u2 += delta
    elif J(u2 - delta) < J(u2):
        u2 -= delta

    delta -=eps


print(u2)
print(J(u2))