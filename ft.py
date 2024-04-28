# muestra de enrollado de frecuencia


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
  rLs = []
  iLs = []
  for k in range(0, size):
    rsum = 0
    isum = 0
    for i in range(0, size):
      f = fun[i] * e**(-2 * pi * i * k * 1j / size)
      rsum += np.real(f)
      isum += np.imag(f)

    rsum /= size
    isum /= size
    rLs.append(rsum)
    iLs.append(isum)
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


# linspace(from, to, number of points)
size = 500
x = np.linspace(0, 10, size)
# create a function that is cos(2.pi.x)
fun = sin(x * pi * 2)

ftransform = ft(fun)

# fig, ax = plt.subplots()
# ax.subplots_adjust(left=0.25, bottom=0.25)
# plt.figure(1)
# plt.plot(x, ftransform, 'red')
# plt.plot(x, ftransform[0], 'red')
# plt.plot(x, ftransform[1], 'gray')

scale = 2

# plt.figure(2)
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider = Slider(ax_slider, 'Valor', 0, 10, valinit=0)  # Los parámetros son (eje, etiqueta, valor mínimo, valor máximo, valor inicial)

# Función que se ejecutará cuando se cambie el valor del deslizador
def update(val):
    global x, fun, fig, ax
    new_value = slider.val
    # plt.figure(2)
    func = updateFun(fun, x, new_value)
    ax.cla()
    # plt.plot(x, fun, 'gray')
    # plt.plot(x, func[0], 'red')
    # plt.plot(x, func[1], 'gray')
    ax.plot(func[0], func[1], 'gray')
    ax.xlim(-2, 2)
    ax.ylim(-2, 2)
    ax.draw()
    
    # plt.draw()
    

slider.on_changed(update)  # Conecta la función "update" al evento "on_changed" del deslizador



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








