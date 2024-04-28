# fft para deviaciones estandares


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
from numpy import cos as cos
from numpy import sin as sin
import time



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

def invFour(frequencies, size):         # creo q no anda
  k = np.linspace(0, size - 1, len(frequencies[0]))
  fun = []

  for n in k:
    fr = frequencies[0] * np.cos(2. * np.pi * k * n / size)
    fi = frequencies[1] * np.sin(2. * np.pi * k * n / size)
    fun.append(sum(fr - fi) / float(size))
  return fun

def mean(fun, size):
  sum = 0
  for i in fun:
    sum += i
  return sum / size

def variance(fun, size, mean):
  sum = 0
  for i in fun:
    sum += (i - mean) ** 2
  return sum / size

def setSdvImg(sdv, size):
  deviationR, deviationI = 0, 0
  for k in range(size):
    sdvR = -1.
    sdvI = -1.
    for n in range(size):
      if(sdvR == -1.):
        sdvR = sdv * np.cos(2. * np.pi * k * n / size)
        sdvR = sdv * np.sin(2. * np.pi * k * n / size)
      else:
        cSdvR = sdv * np.cos(2. * np.pi * k * n / size)
        cSdvI = sdv * np.sin(2. * np.pi * k * n / size)
        sdvR = (sdvR * sdvR + cSdvR * cSdvR)**0.5
        sdvI = (sdvI * sdvI + cSdvI * cSdvI)**0.5
    deviationR += sdvR / size
    deviationI += sdvI / size
    # print("sdv f:", k, ", ", sdvR, "    ", sdvI)
  print("estimateds sdv:", deviationR, "    ", deviationI)

def setVarImg(var, size):
  varianceR, varianceI = 0, 0
  for k in range(size):
    varR = 0.
    varI = 0.
    for n in range(size):
      cvarR = var * (np.cos(2. * np.pi * k * n / size)**2)
      cvarI = var * (np.sin(2. * np.pi * k * n / size)**2)
      varR += cvarR
      varI += cvarI
    print("var f:", k, ", ", varR, "    ", varI)
    varianceR += varR / size
    varianceI += varI / size
  print("estimated var: ", varianceR, "    ", varianceI)

def fastSetVarImg(var, size):
  cR = 0.
  cI = 0.
  for k in range(size):
    cR += np.cos(2. * np.pi * k / size)**2
    cI += np.sin(2. * np.pi * k / size)**2

  varianceR = var * cR
  varianceI = var * cI
  print("original var: ", var)
  print("original sdv: ", var**0.5)
  print("fast estimated var: ", varianceR, "    ", varianceI)
  print("fast estimated sdv: ", varianceR**0.5, "    ", varianceI**0.5)

  # print("estimated var: ", varianceR, "    ", varianceI, "    o: ", varianceR**0.5, "    ", varianceI**0.5)
      
def correctMean(fun, size):
  m = mean(fun, size)
  fun2 = []
  for i in range(size):
    fun2.append(fun[i] - m) 
  return fun

def normalize(fun, size):
  prom = fun[0]
  for i in fun:
    if(prom < i):
      prom = i
  fun /= prom
  return fun
    

size = 16
x = np.linspace(0, size - 1, size)
# x = np.linspace(0, 10, size * 50)

a = x / size
# fun = cos(a * np.pi)
sdv = 10

fun = np.random.normal(0, sdv, size)
# fun = normalize(fun, size)
fun = correctMean(fun, size)



funMean = mean(fun, size)
funVariance = variance(fun, size, funMean)
funSdv = funVariance**0.5
print("Mean: ", funMean)
print("Variance: ", funVariance)
print("Sdv: ", funSdv)

# setSdvImg(funSdv, size)
setVarImg(funVariance, size)
fastSetVarImg(funVariance, size)


frequencies = four(fun, size)

ftMean = mean(frequencies[0], size)
ftVariance = variance(frequencies[0], size, 0)#ftMean)
ftSdv = ftVariance**0.5
print("ft mean: ", ftMean)
print("ft variance: ", ftVariance)
print("ft sdv: ", ftSdv)


'''reFun = invFour(frequencies, size)
plt.figure(1)

plt.plot(x, frequencies[0], 'gray')

plt.xlim(-1, size)
yScale = 600
plt.ylim(-yScale, yScale)


def update(val):
  fun = np.random.normal(0, sdv, size)

  frequencies = four(fun, size)
  plt.figure(1)

  # plt.plot(x, fun, 'r')
  plt.plot(x, frequencies[1], 'gray')

anim = animation.FuncAnimation(plt.gcf(), update, interval=33)


plt.show()
'''



