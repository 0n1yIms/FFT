import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import cos as cos
from numpy import sin as sin
import time
import math
from math import log
from math import pi

pi = 3.1415926535897932384626433832795
e = 2.71828182845904523536028747135

def four(fun, size):
  n = np.linspace(0, size - 1, len(fun))
  frequenciesR = np.zeros(size)
  frequenciesI = np.zeros(size)
  frequenciesR = []
  frequenciesI = []
  for k in n:
    fr = fun * np.cos(2. * np.pi * k * n / size)
    fi = fun * np.sin(2. * np.pi * k * n / size) * (-1.)
    frequenciesR.append(np.sum(fr))
    frequenciesI.append(np.sum(fi))
  return frequenciesR, frequenciesI

def invFour(frequencies, size):
  k = np.linspace(0, size - 1, len(frequencies[0]))
  fun = []

  for n in k:
    fr = frequencies[0] * np.cos(2. * np.pi * k * n / size)
    fi = frequencies[1] * np.sin(2. * np.pi * k * n / size)
    fun.append(sum(fr - fi) / float(size))
  return fun



def ft2d(img, size):
    outR = np.zeros((size, size))
    outI = np.zeros((size, size))

    for ky in range(0, size):
      for kx in range(0, size):
        real = 0
        imag = 0
        for ny in range(0, size):
          for nx in range(0, size):
            titaX = 2 * pi * kx * nx / size
            titaY = 2 * pi * ky * ny / size
            real += img[nx][ny] * cos(titaX + titaY)
            imag -= img[nx][ny] * sin(titaX + titaY)
        outR[kx][ky] = real
        outI[kx][ky] = imag
    return outR, outI


def mult(a, b):
  return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]
def sum(a, b):
  return a[0] + b[0], a[1] + b[1]

def ft2dm(fun, size):
  out = np.zeros((size, size), dtype=tuple)
  outR = np.zeros((size, size))
  outI = np.zeros((size, size))
  funT = np.zeros((size, size), dtype=tuple)
  
  for ky in range(0, size):
    for kx in range(0, size):
      real, imag = 0, 0
      for n in range(0, size):
        tita = 2 * pi * kx * n / size
        real += fun[n][ky] * cos(tita)
        imag -= fun[n][ky] * sin(tita)
      funT[kx][ky] = real, imag

  for kx in range(0, size):
    for ky in range(0, size):
      real, imag = 0, 0
      real2, imag2 = 0, 0
      num = 0, 0
      for n in range(0, size):
        tita = 2 * pi * ky * n / size
        num = sum(num, mult(funT[kx][n], (cos(tita), -1*sin(tita))))
      outR[kx][ky] = num[0]
      outI[kx][ky] = num[1]
  
  return outR, outI
  # return out

'''
size = 16
x = np.zeros((size, size))


for i in range(size):
  for j in range(size):
    x[i][j] = i * j

import time

t0 = time.time()
ft2 = ft2d(x, size)
t1 = time.time()
nTime = t1 - t0
print("time: ", nTime)
t0 = time.time()
ft22 = ft2dm(x, size)
t1 = time.time()
tpTime = t1 - t0
print("time2: ", tpTime)

print(nTime / tpTime * 100, "%")'''

# np.set_printoptions(precision=2, suppress=True)

# print(ft2[0])
# print(ft22[0])
# print("imag:")
# print(ft2[1])
# print(ft22[1])

# def fft(double complex *x, int n, double complex *twf, double complex *a):

			
def cRound(x, n=2):
  return round(x.real, n) + round(x.imag, n) * 1j
      
nodes = [8, 4, 2, 1]
lvls = 4 #[0, 1, 2, 3]
def idx(lvl, fq, nd):
  return int(lvl * 8 + int(fq) * nodes[lvl] + int(nd))

def ft(img):
  n = len(img)
  m = int(math.log(n, 2))
  nodes = [8, 4, 2, 1]
  fqLens = [1, 2, 4, 8]

  ls = np.zeros(32, dtype=complex)
  for nd in range(0, int(nodes[0])):
    index = 0
    for i in range(m):
      index += 2**i * ((nd % 2**(m-i)) // 2**(m-(i+1)))
    ls[idx(0, 0, nd)] = img[int(index)]
    
  for lvl in range(1, lvls):
    node = nodes[lvl]
    fqLen = fqLens[lvl]
    for fq in range(0, fqLen):
      for nd in range(0, node):
        # cidx = idx(lvl, fq, nd)
        # lidx = idx(lvl - 1,fq % fqLens[lvl - 1], 2 * nd), \
          # idx(lvl - 1, fq % fqLens[lvl - 1], 2 * nd + 1)
        # nn = ls[lidx[0]]
        # nn2 = ls[lidx[1]]
        # ne = e**(-2j*pi*fq/fqLen)
        num = \
          ls[idx(lvl - 1,fq % fqLens[lvl - 1], 2 * nd)] + \
          ls[idx(lvl - 1, fq % fqLens[lvl - 1], 2 * nd + 1)] \
            * e**(-2j*pi*fq/fqLen)
        ls[idx(lvl, fq, nd)] = num
    # rls = [cRound(x) for x in ls[idx(lvl, 0, 0):idx(lvl, 0, 0) + 8]]
  
    # print("lvl", lvl, rls)
    # print("lvl", lvl, ls[idx(lvl - 1, 0, 0):idx(lvl - 1, 0, 0) + 8])
  return ls

nodesFft = []
nFft = 0
def idxFt(lvl, fq, node):
  return lvl * nFft + fq * nodesFft[lvl] + node

def fftAlg(img):
  n = len(img)  # 8
  m = int(log(n, 2)) # 3
  lvls = m + 1
  nodes = [2**i for i in range(m, -1, -1) ] # [8, 4, 2, 1]
  fqLens = [2**i for i in range(0, m + 1)] # [1, 2, 4, 8]
  global nodesFft
  nodesFft = nodes
  global nFft
  nFft = n

  ls = np.zeros(n * lvls, dtype=complex)
  for x in range(0, nodes[0]):
    index = 0
    for i in range(m):
      index += 2**i * ((x % 2**(m-i)) // 2**(m-(i+1)))
    ls[idxFt(0, 0, x)] = img[int(index)]
      
  for lvl in range(1, lvls):
    node = nodes[lvl]
    fqLen = fqLens[lvl]
    for fq in range(0, fqLen):
      for nd in range(0, node):
        ls[idxFt(lvl, fq, nd)] = \
          ls[idxFt(lvl - 1,fq % fqLens[lvl - 1], 2 * nd)] + \
          ls[idxFt(lvl - 1, fq % fqLens[lvl - 1], 2 * nd + 1)] \
          * e**(-2j*pi*fq/fqLen)
  
  return ls[n*m:n*(m+1)]
  # return ls[24:32]
    
    
def ifftAlg(img):  
  img = [x.real - x.imag*1j for x in img]


  n = len(img)  # 8
  m = int(log(n, 2)) # 3
  lvls = m + 1
  nodes = [2**i for i in range(m, -1, -1) ] # [8, 4, 2, 1]
  fqLens = [2**i for i in range(0, m + 1)] # [1, 2, 4, 8]
  global nodesFft
  nodesFft = nodes
  global nFft
  nFft = n

  ls = np.zeros(n * (m + 1), dtype=complex)
  for x in range(0, nodes[0]):
    index = 0
    for i in range(m):
      index += 2**i * ((x % 2**(m-i)) // 2**(m-(i+1)))
    ls[idxFt(0, 0, x)] = img[int(index)]
      
  for lvl in range(1, lvls):
    node = nodes[lvl]
    fqLen = fqLens[lvl]
    for fq in range(0, fqLen):
      for nd in range(0, node):
        ls[idxFt(lvl, fq, nd)] = \
          ls[idxFt(lvl - 1,fq % fqLens[lvl - 1], 2 * nd)] + \
          ls[idxFt(lvl - 1, fq % fqLens[lvl - 1], 2 * nd + 1)] \
          * e**(-2j*pi*fq/fqLen)
  
  ls = ls[n*m:n*(m+1)]
  ls = [x / n for x in ls]
  return ls
    


def invF8(frequencies, size):
  k = np.linspace(0, size - 1, size)
  fun = []

  for n in k:
    # fr = frequencies[:].real * np.cos(2. * np.pi * k * n / size)
    # fi = frequencies[:].imag * np.sin(2. * np.pi * k * n / size)
    fr = frequencies[0] * np.cos(2. * np.pi * k * n / size)
    fi = frequencies[1] * np.sin(2. * np.pi * k * n / size)
    fun.append(np.sum(fr - fi) / float(size))
  return fun

def invF8C(frequencies, size):
  k = np.linspace(0, size - 1, size)
  fun = []
  for n in k:
    ni = frequencies[:] * e**(2j * pi * k * n / size)
    fun.append(np.sum(ni) / float(size))
    
    # fr = frequencies[:].real * np.cos(2. * np.pi * k * n / size)
    # fi = frequencies[:].imag * np.sin(2. * np.pi * k * n / size)
    # fun.append(np.sum(fr - fi) / float(size))
    
    # fr = frequencies[0] * np.cos(2. * np.pi * k * n / size)
    # fi = frequencies[1] * np.sin(2. * np.pi * k * n / size)
    # fun.append(np.sum(fr - fi))
    # fun = [cRound(x) for x in fun]
  return fun
   
def conj(x):
  return x.real - x.imag*1j

ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

fftLs = fftAlg(ls)
ifftLs = ifftAlg(fftLs)

# ifftLs = invF8C(fftLs, 8)

fftLs = [cRound(x) for x in fftLs]
ifftLs = [cRound(x) for x in ifftLs]

print(fftLs)
print(ifftLs)



# nft = four(ls, 8)
# nft = FFT(ls)
# ift = invF8(nft, 8)

# nft = np.fft.fft(ls)
# ift = np.fft.ifft(nft)
# nft = [cRound(x) for x in nft]
# ift = [cRound(x) for x in ift]
# print("nft: ", nft)
# print("ift: ", ift)

# nft = four(ls, 8)
# nift = invF8(nft, 8)

# nft = [round(x, 2) for x in nft[0]], [round(x, 2) for x in nft[1]]
# nift = [round(x, 2) for x in nift]

# print("fft", nft)
# print("ift", nift)

# fastft = ft(ls)
# fastift = invF8C(fastft[24:32], 8)

# fastft = [cRound(x) for x in fastft]
# fastift = [cRound(x) for x in fastift]
# print("fft", fastft[24:32])
# print("ifft: ", fastift)


# print("fft", fls[24:32])
# print("ifft: ", ifft)
