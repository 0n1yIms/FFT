# Discrete Fourier Transform
Discrete fourier transform implementations


## Normal DFT Algoritm
N = 16

>for ky -> size:
&nbsp;for kx -> size:
&nbsp;&nbsp;real, imag = 0, 0
&nbsp;&nbsp;for ny -> size:
&nbsp;&nbsp;&nbsp;for nx -> size:
&nbsp;&nbsp;&nbsp;&nbsp;$\ real = real + img(nx,ny) *
cos(\frac{2 \pi.kx.nx}{N} + \frac{2 \pi.ky.ny}{N}) $
&nbsp;&nbsp;&nbsp;&nbsp;$\ imag = imag + img(nx,ny) *
-sin(\frac{2 \pi kx.nx}{N} + \frac{2 \pi.ky.ny}{N}) $
&nbsp;&nbsp;$\ F_{r} = real $
&nbsp;&nbsp;$\ F_{i} = imag $


real operations = $\ 2.size^{2} $
imag operations = $\ 2.size^{2} $
complex operations = $\ 2.2.size^{2}  = 4size^{2} $
F opeations = $\ size^{2}.4.size^{2} = 4.size^{4} $

## Two passes DFT algorithm
N = 16

>for ky -> size:
&nbsp;for kx -> size:
&nbsp;&nbsp;num = 0, 0
&nbsp;&nbsp;for n -> size:
&nbsp;&nbsp;&nbsp;$\ num = num_{R} + img_{n,ky} *
cos(\frac{2 \pi.kx.n}{N}), num_{I} + img_{n,ky} *
-sin(\frac{2 \pi.kx.n}{N})$
&nbsp;&nbsp;$\ F = num $
for ky -> size:
&nbsp;for kx -> size:
&nbsp;&nbsp;num = 0, 0
&nbsp;&nbsp;for n -> size:
&nbsp;&nbsp;&nbsp;$\ real = real + F(k_{x},n)_{R} *
cos(\frac{2 \pi k_{y} n}{N}) - F(k_{x}, n)_{I} * -sin(\frac{2 \pi k_{y} n}{N}) $
&nbsp;&nbsp;&nbsp;$\ imag = imag + F(k_{x},n)_{R} *
-sin(\frac{2 \pi k_{y} n}{N})  + F(k_{x},n)_{I} * cos(\frac{2 \pi k_{y} n}{N}) $
&nbsp;&nbsp;$\ F_{r} = real $
&nbsp;&nbsp;$\ F_{i} = imag $


num 1 operations = $\ 2.2.size = 4.size $

real operations = $\ 4.size $
imag operations = $\ 4.size $
cmpx operations = $\ 16.size $

F opeations = $\ size^{2}.4.size + size^{2}.16.size 
= 4.size^{3} + 16.size^{3} = 20.size^{3} $

## DFT algorithms complexity differences
Normal DFT complexity:
$\ 4.size^{4} $
Two passes DFT algorithm:
$\ 20.size^{3} $

size = 16
$\ 4.16^{4} = 4.65536 = 262144 $
$\ 20.16^{3} = 20.4096 = 81920 $
$\ \frac{262144}{81920}.100 = 320 $
The N DFT seems to be 320% slower than the TP DFT algorithm

## FFT algorithm
Works only with powers of two

###### Vars:
- size


> for lvl in (1, $\ log_{2}(n) $)
&nbsp;nodes = $\ 2^{lvl} $
&nbsp;shift = floor( $\frac{n}{nodes} $)

>num = 0, 0
for n -> size:
&nbsp;$\ num = num_{R} + img_{n} *
cos(\frac{2 \pi.k.n}{N}), num_{I} + img_{n} *
-sin(\frac{2 \pi.k.n}{N})$
&nbsp;$\ F = num $


num operations = $\ 2.2.size = 4.size $

real operations = $\ 4.size $
imag operations = $\ 4.size $
cmpx operations = $\ 16.size $

F opeations = $\ size^{2}.4.size + size^{2}.16.size 
= 4.size^{3} + 16.size^{3} = 20.size^{3} $


# FFT
Lets suppose we have a discrete function with length 8, _len = 8_.
Now we divide it by two, and repeat


8
4 , 4
2, 2 | 2, 2
1, 1 | 1, 1 | 1, 1 | 1, 1

we needs this
8 imgs 
4 imgs
2 imgs
1 img


split levels = $\ log_{2}(8) = 3 (1, 2, 3) $
nodes = $\ 2^{level} $ = (2, 4, 8)
nLen = 8 / nodes = (4, 2, 1)

for lvl 1:
&nbsp;node = 2
&nbsp;nLen = 4

N = 4

[a],[b],[c],[d]
[(a + c), (a + fc)][(c + d),(c + fd)]
[     a0         ,    b0            ]
[a0 + f(b0)]


###$ \sum_{n = 1}^{N} x_{n}.e^{\frac{-2.i.\pi.k.n}{N}} $

###$ \sum_{n = 1}^{N/2} x_{2n}.e^{\frac{-2.i.\pi.k.2n}{N}} + \sum_{n = 1}^{N/2} x_{2n+1}.e^{\frac{-2.i.\pi.k.(2n + 1)}{N}} $

###$ \sum_{n = 1}^{N/2} x_{2n}.e^{\frac{-2.i.\pi.k.n}{N/2}} + e^{\frac{-2.i.\pi.k}{N}}.\sum_{n = 1}^{N/2} x_{2n+1}.e^{\frac{-2.i.\pi.k.2n}{N}} $

###$ \sum_{n = 1}^{N/2} x_{2n}.e^{\frac{-2.i.\pi.k.n}{N/2}} + e^{\frac{-2.i.\pi.k}{N}}.\sum_{n = 1}^{N/2} x_{2n+1}.e^{\frac{-2.i.\pi.k.n}{N/2}} $

###$ \sum_{n = 1}^{N/4} x_{4n}.e^{\frac{-2.i.\pi.k.2n}{N/2}} + \sum_{n = 1}^{N/4} x_{4n + 2}.e^{\frac{-2.i.\pi.k.(2n + 1)}{N/2}} + e^{\frac{-2.i.\pi.k}{N}}.\left[\sum_{n = 1}^{N/4} x_{2(2n)+1}.e^{\frac{-2.i.\pi.k.2n}{N/2}} + \sum_{n = 1}^{N/4} x_{2(2n + 1) + 1}.e^{\frac{-2.i.\pi.k.(2n + 1)}{N/2}}\right]$


###$ \sum_{n = 1}^{N/4} x_{4n}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N/2}}.\sum_{n = 1}^{N/4} x_{4n + 2}.e^{\frac{-2.i.\pi.k.2n}{N/2}} + e^{\frac{-2.i.\pi.k}{N}}.\left[\sum_{n = 1}^{N/4} x_{2(2n)+1}.e^{\frac{-2.i.\pi.k.2n}{N/2}} + \sum_{n = 1}^{N/4} x_{2(2n + 1) + 1}.e^{\frac{-2.i.\pi.k.(2n + 1)}{N/2}}\right]$

###$ \sum_{n = 1}^{N/4} x_{4n}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N/2}}.\sum_{n = 1}^{N/4} x_{4n + 2}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N}}.\left[\sum_{n = 1}^{N/4} x_{4n+1}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N/2}}.\sum_{n = 1}^{N/4} x_{4n + 3}.e^{\frac{-2.i.\pi.k.2n}{N/2}}\right]$

###$ \sum_{n = 1}^{N/4} x_{4n}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N/2}}.\sum_{n = 1}^{N/4} x_{4n + 2}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N}}.\left[\sum_{n = 1}^{N/4} x_{4n+1}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N/2}}.\sum_{n = 1}^{N/4} x_{4n + 3}.e^{\frac{-2.i.\pi.k.n}{N/4}}\right]$

N = 4

###$ x_{0}.e^{-2.i.\pi.k} + e^{\frac{-2.i.\pi.k}{2}}.x_{2}.e^{-2.i.\pi.k} + e^{\frac{-2.i.\pi.k}{4}}.\left[x_{1}.e^{-2.i.\pi.k} + e^{\frac{-2.i.\pi.k}{2}}.x_{3}.e^{-2.i.\pi.k}\right]$

__Formula__
###$ x_{0} + e^{\frac{-2.i.\pi.k}{2}}.x_{2} + e^{\frac{-2.i.\pi.k}{4}}.\left[x_{1} + e^{\frac{-2.i.\pi.k}{2}}.x_{3}\right]$

<!-- ###$ A = \left[x_{0}, x_{1}, x_{2}, x_{3} \right]$ -->
###$ A = \left[x_{0} \right]$
###$ B = \left[x_{1} \right]$
###$ C = \left[x_{2} \right]$
###$ D = \left[x_{3} \right]$
---
###$ A = \left[(x_{0}, x_{1}) + e^{\frac{-2.i.\pi.0}{2}}.(x_{2}, x_{3}) \right] $
###$ B = \left[(x_{0}, x_{1}) + e^{\frac{-2.i.\pi.1}{2}}.(x_{2}, x_{3}) \right] $
---

###$ \left[(A, B) + e^{\frac{-2.i.\pi.0}{4}}.(A, B) \right] \left[(A, B) + e^{\frac{-2.i.\pi.1}{4}}.(A, B) \right] \left[(A, B) + e^{\frac{-2.i.\pi.2}{4}}.(A, B) \right] \left[(A, B) + e^{\frac{-2.i.\pi.3}{4}}.(A, B) \right]$


levels =(1, 2, 3) = 3
nodes = (1, 2, 4)
nNums = (4, 2, 1)

ls [4.1 + 2.2 + 1.4] = [12]

>for lvl in levels:
&nbsp;nd = nodes[lvl]
&nbsp;for nIdx in nNums[lvl]
&nbsp;&nbsp;ls[nd][nIdx] = $ e^{\frac{-2.i.\pi.nIdx}{nd}} $ .ls[nd - 1][nIdx / 2]





N = 8

###$ x_{0} + e^{\frac{-2.i.\pi.k}{2}}.x_{2} + e^{\frac{-2.i.\pi.k}{4}}.\left[x_{1} + e^{\frac{-2.i.\pi.k}{2}}.x_{3}\right]$
---
###$ \left[x_{0}, x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}, x_{7} \right]$

---

###$ x_{0} = \left[(x_{0}, x_{1}, x_{2},x_{3}) + e^{\frac{-2.i.\pi.0}{2}}.(x_{4}, x_{5}, x_{6}, x_{7}) \right] $
###$ x_{1} = \left[(x_{0}, x_{1}, x_{2},x_{3}) + e^{\frac{-2.i.\pi.1}{2}}.(x_{4}, x_{5}, x_{6}, x_{7}) \right] $

---

###$ x_{0} = \left[(x_{0}, x_{1}) + e^{\frac{-2.i.\pi.0}{2}}.(x_{4}, x_{5}, x_{6}, x_{7}) \right] $

---

###$\left[(A, B, C, D) + e^{\frac{-2.i.\pi.0}{8}}.(A, B, C, D) \right] $
###$\left[(A, B, C, D) + e^{\frac{-2.i.\pi.1}{8}}.(A, B, C, D) \right] $
###$\left[(A, B, C, D) + e^{\frac{-2.i.\pi.2}{8}}.(A, B, C, D) \right] $
###$\left[(A, B, C, D) + e^{\frac{-2.i.\pi.3}{8}}.(A, B, C, D) \right] $
###$\left[(A, B, C, D) + e^{\frac{-2.i.\pi.4}{8}}.(A, B, C, D) \right] $
###$\left[(A, B, C, D) + e^{\frac{-2.i.\pi.5}{8}}.(A, B, C, D) \right] $
###$\left[(A, B, C, D) + e^{\frac{-2.i.\pi.6}{8}}.(A, B, C, D) \right] $
###$\left[(A, B, C, D) + e^{\frac{-2.i.\pi.7}{8}}.(A, B, C, D) \right] $


&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;