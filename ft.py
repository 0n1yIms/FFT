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

def ft(fun, x, freq):
  rLs = []
  iLs = []
  vecmod = []
  for i in freq:
    f = fun * e**(-pi * x * 1j * i)
    freal = f.real
    fimag = f.imag
    nReal = len(freal)
    nImag = len(fimag)
    rSum = sum(freal) / nReal
    iSum = sum(fimag) / nImag
    rLs.append(rSum)
    iLs.append(iSum)
    # vecmod.append(np.sqrt(rSum**2 + iSum**2))
  # vecmod = np.sqrt(rLs * rLs + iLs * iLs)
  # return vecmod
  return rLs, iLs

def ift(fun, x):
  f = list(fun[0])
  for i in range(0, size * 50):
    iv = i / 50
    fr = fun[0][i] * cos(-iv * x * pi)
    fi = fun[1][i] * sin(-iv * x * pi)
    f += fr + fi
    # f += fi

  f = f / 2
  # f /= (size)
  return f



size = 10
x = np.linspace(0,size, 50 * size)
# x = np.linspace(0,size)
fun = sin(x * pi * 2)
# fun = cos(x * pi * 2)

freq = np.linspace(0, size, 50 * size)
# ftransform = ft(fun, x, freq)
# invft = ift(ftransform, x)
# freq = 0
ftransform = updateFun(fun, x, freq)
# integralF = integral(ftransform, x)


# fig, ax = plt.subplots()
# ax.subplots_adjust(left=0.25, bottom=0.25)
plt.figure(1)
plt.plot(x, ftransform, 'red')
# plt.plot(x, ftransform[0], 'red')
# plt.plot(x, ftransform[1], 'gray')

scale = 4
plt.xlim(0, scale)
plt.ylim(-scale, scale)

plt.figure(2) 
# plt.plot(x, invft, 'gray')
plt.plot(x, fun, 'cyan')
plt.xlim(0, scale)
plt.ylim(-scale, scale)


# plt.figure(2)
# axfreq = plt.axes([0.2, 0.1, 0.5, 0.03])
# freqq = Slider(axfreq, 'Frequency', 0.0, size / 2, 0)


def update(val):
  global x, fun, freq, ftransform, integralF
  # freq += 0.01
  freq = val
  ftransform = updateFun(fun, x, freq)
  integralF = integral(ftransform, x) 
  plt.figure(1)
  plt.cla()
  plt.xlim(-scale, scale)
  plt.ylim(-scale, scale)
  plt.plot(ftransform[0], ftransform[1], 'gray')
  plt.scatter([0, integralF[0]], [0, integralF[1]])
  plt.draw()
    
# freqq.on_changed(update)
# anim = animation.FuncAnimation(plt.gcf(), update, interval=50)

plt.show()

# plt.plot(freq, fun, 'gray')
# plt.plot(freq, ftransform[0], 'gray')
# plt.plot(freq, ftransform[1], 'blue')
#plt.plot(integralF[0],integralF[1],'ro')

# plt.figure(1)
# def update(i):
#   global freq
#   global fun
#   if freq < 10:
#     freq += 0.005
#   print(freq)
#   f = updateFun(fun, x, freq)
#   integralF = integral(f, x)
#   plt.cla()
#   plt.plot(f[0],f[1])
#   plt.plot(integralF[0],integralF[1],'ro')
# anim = animation.FuncAnimation(plt.gcf(), update, interval=10)








