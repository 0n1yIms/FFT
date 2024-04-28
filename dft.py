import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import cos as cos
from numpy import sin as sin
import time

pi = 3.1415
e = 2.71828182845904523536028747135


def updateFun(fun, x, freq):
  f = fun * e**(pi * x * 1j * freq)
  return np.real(f), np.imag(f)

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

def ift(fun, freq):
  ls = []
  xFun = list(range(len(freq)))
  x = np.linspace(0, len(freq))
  for i in range(len(freq)):
    xFun += fun[0][i] * cos(pi * i * x)
    xFun += fun[1][i] * sin(pi * i * x)
    
    
  return xFun


size = 10
x = np.linspace(0,size)
fun = cos(x * pi / 2)

freq = np.linspace(0, size)

ds = ft(fun, x, freq)

ss = ift(ds, freq)
plt.plot(x, ss,'-o', color='gray')

# plt.scatter(x, ds[0])
# plt.plot(x, fun,'-o', color='gray')
# plt.plot(x, ds[0],'-o', color='gray')
# plt.plot(x, ds[1],'-o', color='red')





def update(i):
  global freq
  global fun
  if freq < 10:
    freq += 0.005
  print(freq)
  f = updateFun(fun, x, freq)
  integralF = integral(f, x)
  plt.cla()
  plt.plot(f[0],f[1])
  plt.plot(integralF[0],integralF[1],'ro')


#anim = animation.FuncAnimation(plt.gcf(), update, interval=10)


plt.show()
