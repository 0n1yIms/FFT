import matplotlib.pyplot as plt
import numpy as np


def FFT(x):
    # N = x.size
    N = len(x)
    
    if N == 1:
        return x
    else:
        # print("split", x, "  in: ", x[::2], x[1::2])
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j*np.pi*np.arange(N)/ N)
        # print("factor: ", factor)
        
        # print(X_even, " + " , factor[:int(N/2)] , " * " , X_odd)
        # print(X_even, " + " , factor[int(N/2):] , " * " , X_odd)
        X = np.concatenate(
            [X_even + factor[:int(N/2)]*X_odd,
             X_even + factor[int(N/2):]*X_odd]
             )
        return X

def IFFT(x):
    # N = x.size
    N = len(x)
    I = FFT(x.conjugate())/N
    

size = 8
x = np.linspace(0, 1, size)

fun = x

# printf fun
print("fun: ", fun)

#apply fft
ft = FFT(fun.tolist())

# print ft
print("ft: ", ft)




# fun = x * x

# plt.figure(figsize = (8, 6))
# plt.plot(x, fun)
# plt.ylabel('Amplitude')
# plt.figure(figsize = (8, 6))
# ft = FFT(fun.tolist())
# plt.plot(x, ft)
# plt.show()