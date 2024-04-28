import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import cos as cos
from numpy import sin as sin
import time



def convole(F, G):
    FL = len(F)
    GL = len(G)
    ls = []
    for n in range(FL + GL - 1):
        sum = 0.
        sl = max(0, -GL + n + 1)
        su = min(n + 1, FL)
        k = sl
        while (k <= su):
            sum += F[k] * G[n - k]
            k+=1

        ls.append(sum)
    return 0


N1 = 32
y = list(range(N1))

for i in range(N1):
    if i < N1 * 0.3 or i > N1 * 0.7:
        y[i] = 0
    else:
        y[i] = 1
    # x[len(x) - i - 1] = 0


g = [0, 1, 2, 3, 2, 1, 0]

conv = convole(y, g)


# plt.plot(x)
plt.scatter(list(len(y)), y)
plt.scatter(list(len(conv)), conv)
plt.show()
