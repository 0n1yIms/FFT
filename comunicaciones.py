import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import cos as cos
from numpy import sin as sin
import time


def fun1(x):
    if x >= 0 and x <= 2:
        return 1
    else:
        return 0
    
def integrate(f, x):
    return np.trapz(f, x)

# show graphic
x = np.linspace(-10, 10, 1000)

plt.plot(x, np.vectorize(fun1)(x))
plt.show()

def ft(k):
    sum = 0
    for n1 in range(-1000, 1000):
        n = n1 / 10
        sum += (fun1(n) * np.e**(-2j * np.pi * k * n)) * 0.1
    return sum

N = 1000
x = np.linspace(-N, N, 2*N+1)
f = np.vectorize(fun1)(x)
ftf = np.vectorize(ft)(x)
mftf = [i.real for i in ftf]

print(ftf)


# ls = [ft(i) for i in x]
# mls = [modulada(i) for i in x]


plt.plot(x, f, color='red')
plt.plot(x, ftf, color='blue')
# plt.plot(mls)
plt.show()
