# Discrete fourier transform

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
from numpy import cos as cos
from numpy import sin as sin
import time

pi = 3.1415
e = 2.71828182845904523536028747135

def updateFun(fun, x, freq):
  f = fun * e**(-2 * pi * x * 1j * freq)
  return np.real(f), np.imag(f)

def integral(fun, x):
  fr = fun[0]
  fi = fun[1]
  nReal = len(fr)
  nImag = len(fi)
  rSum = sum(fr) / nReal
  iSum = sum(fi) / nImag
  return rSum, iSum

def ft(fun):
  size = len(fun)
  ls = []
  for k in range(0, size):
    sum = 0
    for i in range(0, size):
      f = fun[i] * e**(2 * pi * i * k * 1j / size)
      sum += f
      # rsum += np.real(f)
      # isum += np.imag(f)

    # rsum /= size
    # isum /= size
    # ls.append(rsum + isum)
    sum /= size
    ls.append(sum)
  return ls

def ift(fun):
  size = len(fun)
  rLs = []
  # iLs = []
  for k in range(0, size):
    rsum = 0
    # isum = 0
    for i in range(0, size):
      f = fun[i] * e**(-2 * pi * i * 1j *k / size)
      rsum += f
      # isum += fi

    rLs.append(rsum)
    # iLs.append(isum)
  return rLs
  # return rLs, iLs


# linspace(from, to, number of points)
size = 8
x = np.linspace(0, 7, size)
ftransform = ft(x)

# print fun
print("fun: ", x)

# print ftransform
print("ftransform: ", ftransform)


# print ift(ftransform, x)
inv = ift(ftransform)
# round to 2 decimals
inv = [round(x, 2) for x in inv]
print("inv: ", inv)

