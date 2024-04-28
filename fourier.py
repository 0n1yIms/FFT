import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import cos as cos
from numpy import sin as sin
import time

#import round



def dft(X):
    N = len(X)
    ls = list(range(N))
    for n in range(N):
        ls[n] = 0
        for k in range(N):
            ls[n] += X[k] * np.e**(-2j * np.pi * k * n / N)
        ls[n] /= N
    return ls

def fastDFT(X):
    N = len(X)
    ls = list(range(N / 2))
    for n in range(N):
        ls[n] = 0
        for k in range(N):
            ls[n] += X[k] * np.e**(-2j * np.pi * k * n / N)
    return ls


N1 = 32
# y = list(range(N1))
y = list(range(N1))

g = [0, 1, 2, 3, 2, 1, 0]

conv = dft(y)

# round to 4 decimals
def roundComplex(x, n=4):
    return round(x.real, n) + round(x.imag, n) * 1j

conv = [roundComplex(x) for x in conv]

print(conv)

plt.plot(y)
plt.plot(conv)


with open('data.txt', 'w') as f:
    for y_val in conv:
        f.write(str(y_val) + '\n')


# plt.plot(x)
# plt.scatter(list(len(y)), y)
# plt.scatter(list(len(conv)), conv)
plt.show()
