from math import *
import numpy as np

def fft(X):
    N = len(X)
    n = int(log(N, 2))

    nodes = [2**(n - i) for i in range(0, n + 1)]
    values = [2**i for i in range(0, n + 1)]

    blocks = [[[] for j in range(N)] for i in range(n + 1)]

    blocks[0] = []
    for i in range(N):
        idx = 0
        for j in range(n):
            idx += 2**j * ((i // (2 ** (n - 1 - j))) % 2)
        blocks[0].append(X[idx])

    for lvl in range(1, n + 1):
        for nd in range(nodes[lvl]):
            for v in range(values[lvl]):
                A = blocks[lvl - 1][values[lvl] * nd + v % values[lvl - 1]]
                B = blocks[lvl - 1][values[lvl] * nd + v % values[lvl - 1] + values[lvl - 1]]

                C = np.e ** (-2j * pi * v / values[lvl])

                blocks[lvl][values[lvl] * nd + v] = A + C * B
    return blocks[n]

def conj(x):
    return x.real - x.imag*1j

X = [2, 3, 4, 8, 7, 6, 5, 4]
N = len(X)

Xfft = fft(X) 
for i in range(N):
    Xfft[i] = Xfft[i] / N

XfftConj = [conj(x) for x in Xfft]
Xifft = fft(XfftConj)

# round
for i in range(N):
    Xfft[i] = round(Xfft[i].real, 4) + round(Xfft[i].imag, 4) * 1j
    Xifft[i] = round(Xifft[i].real, 4) + round(Xifft[i].imag, 4) * 1j

# print(Xfft)
# print(Xifft)

# vector fft
    

def fftv(X):
    N = len(X)
    n = int(log(N, 2))
    lvls = n + 1

    nodes = [2**(n - i) for i in range(0, lvls)]
    values = [2**i for i in range(0, lvls)]

    Coef = [([np.e ** (-2j * pi * v / values[lvl]) for v in range(values[lvl])]) for lvl in range(lvls)]

    print("real:")
    for lvl in range(lvls):
        for v in range(values[lvl]):
            print (f"{Coef[lvl][v].real:.15f},")

    print("imag:")
    for lvl in range(lvls):
        for v in range(values[lvl]):
            print (f"{Coef[lvl][v].imag:.15f},")


    blocks = [[[] for j in range(N)] for i in range(lvls)]

    blocks[0] = []
    for i in range(N):
        idx = 0
        for j in range(n):
            idx += 2**j * ((i // (2 ** (n - 1 - j))) % 2)
        blocks[0].append(X[idx])

    for lvl in range(1, lvls):
        for nd in range(nodes[lvl]):
            for v in range(values[lvl]):
                A = blocks[lvl - 1][values[lvl] * nd + v % values[lvl - 1]]
                B = blocks[lvl - 1][values[lvl] * nd + v % values[lvl - 1] + values[lvl - 1]]

                C = Coef[lvl][v]
                # C = np.e ** (-2j * pi * v / values[lvl])

                blocks[lvl][values[lvl] * nd + v] = A + C * B
    return blocks[n]

X = [2, 3, 4, 8, 7, 6, 5, 4]
N = len(X)

Xfft = fftv(X) 
for i in range(N):
    Xfft[i] = Xfft[i] / N

XfftConj = [conj(x) for x in Xfft]
Xifft = fftv(XfftConj)

# round
for i in range(N):
    Xfft[i] = round(Xfft[i].real, 4) + round(Xfft[i].imag, 4) * 1j
    Xifft[i] = round(Xifft[i].real, 4) + round(Xifft[i].imag, 4) * 1j

# print(Xfft)
# print(Xifft)







