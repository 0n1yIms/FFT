import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import cos as cos
import time

pi = 3.1415926535897932384626433832795
e = 2.71828182845904523536028747135

def updateFun(fun, x, freq):
  f = fun * cos(pi * x * freq)
  return f

def integral(fun, x):
  fr = fun[0]
  fi = fun[1]
  nReal = len(fr)
  nImag = len(fi)
  rSum = sum(fr) / nReal
  iSum = sum(fi) / nImag
  return rSum, iSum

def ft(fun, x, freq):
  rLs = []
  iLs = []
  for i in freq:
    f = fun * e**(pi * x * 1j * i)
    freal = f.real
    fimag = f.imag
    nReal = len(freal)
    nImag = len(fimag)
    rSum = sum(freal) / nReal
    iSum = sum(fimag) / nImag
    rLs.append(rSum)
    iLs.append(iSum)
  return rLs, iLs


# create a function that is cos(x * pi * 2)
size = 10
x = np.linspace(0,size, size * 50)
fun = cos(x * pi * 2)

freq = 0
f = updateFun(fun, x, freq)

plt.plot(x, f)

def update(i):
  global freq
  global fun
  if freq < 10:
    freq += 0.005
  print(freq)
  f = updateFun(fun, x, freq)
  plt.cla()
  plt.plot(x,fun, 'gray')
  plt.plot(x,f)


anim = animation.FuncAnimation(plt.gcf(), update, interval=10)
plt.show()






