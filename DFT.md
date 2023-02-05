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

#### Level 1
---

###$ \left[x_{0}, x_{1}, x_{2}, x_{3} \right] = A $

---

###$ \left[A_{0} + e^{\frac{-2.i.\pi.0}{2}}.A_{2}, A_{1} + e^{\frac{-2.i.\pi.0}{2}}.A_{3} \right] = [A_{0}, A_{1}] = A $
###$ \left[A_{0} + e^{\frac{-2.i.\pi.1}{2}}.A_{2}, A_{1} + e^{\frac{-2.i.\pi.1}{2}}.A_{3} \right] = [B_{0}, B_{1}] = B $

---

###$ \left[A_{0} + e^{\frac{-2.i.\pi.0}{4}}.A_{1} \right] = A $
###$ \left[B_{0} + e^{\frac{-2.i.\pi.1}{4}}.B_{1} \right] = B $
###$ \left[A_{0} + e^{\frac{-2.i.\pi.2}{4}}.A_{1} \right] = C $
###$ \left[B_{0} + e^{\frac{-2.i.\pi.3}{4}}.B_{1} \right] = D $

---

###$ \left[(A, B)_{0} + e^{\frac{-2.i.\pi.0}{4}}.(A, B)_{0} \right] $ 
###$ \left[(A, B)_{1} + e^{\frac{-2.i.\pi.1}{4}}.(A, B)_{1} \right] $ 
###$ \left[(A, B)_{0} + e^{\frac{-2.i.\pi.2}{4}}.(A, B)_{0} \right] $ 
###$ \left[(A, B)_{1} + e^{\frac{-2.i.\pi.3}{4}}.(A, B)_{1} \right] $ 

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
####$ \left[x_{0}, x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}, x_{7} \right] = A $

---

####$ \left[A_{0} + e^{\frac{-2.i.\pi.0}{2}}.A_{4}, A_{1} + e^{\frac{-2.i.\pi.0}{2}}.A_{5}, A_{2} + e^{\frac{-2.i.\pi.0}{2}}.A_{6}, A_{3} + e^{\frac{-2.i.\pi.0}{2}}.A_{7} \right] = [A_{0}, A_{1}, A_{2}, A_{3}] = A $

####$ \left[B_{0} + e^{\frac{-2.i.\pi.0}{2}}.B_{4}, B_{1} + e^{\frac{-2.i.\pi.0}{2}}.B_{5}, B_{2} + e^{\frac{-2.i.\pi.0}{2}}.B_{6}, B_{3} + e^{\frac{-2.i.\pi.0}{2}}.B_{7} \right] = [B_{0}, B_{1}, B_{2}, B_{3}] = B $

---

####$ \left[A_{0} + e^{\frac{-2.i.\pi.0}{2}}.A_{4}, A_{1} + e^{\frac{-2.i.\pi.0}{2}}.A_{5}, A_{2} + e^{\frac{-2.i.\pi.0}{2}}.A_{6}, A_{3} + e^{\frac{-2.i.\pi.0}{2}}.A_{7} \right] = [A_{0}, A_{1}, A_{2}, A_{3}] = A $

---

###$ \left[(A, B)_{0} + e^{\frac{-2.i.\pi.0}{4}}.(A, B)_{0} \right] $ 
###$ \left[(A, B)_{1} + e^{\frac{-2.i.\pi.1}{4}}.(A, B)_{1} \right] $ 
###$ \left[(A, B)_{0} + e^{\frac{-2.i.\pi.2}{4}}.(A, B)_{0} \right] $ 
###$ \left[(A, B)_{1} + e^{\frac{-2.i.\pi.3}{4}}.(A, B)_{1} \right] $ 


&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;


### FFT
$ \sum_{n = 1}^{N} x_{n}.e^{\frac{-2.i.\pi.k.n}{N}} $

$ \sum_{n = 1}^{N/2} x_{2n}.e^{\frac{-2.i.\pi.k.2n}{N}} + \sum_{n = 1}^{N/2} x_{2n+1}.e^{\frac{-2.i.\pi.k.(2n + 1)}{N}} $

$ \sum_{n = 1}^{N/2} x_{2n}.e^{\frac{-2.i.\pi.k.n}{N/2}} + e^{\frac{-2.i.\pi.k}{N}}.\sum_{n = 1}^{N/2} x_{2n+1}.e^{\frac{-2.i.\pi.k.2n}{N}} $

$ \sum_{n = 1}^{N/2} x_{2n}.e^{\frac{-2.i.\pi.k.n}{N/2}} + e^{\frac{-2.i.\pi.k}{N}}.\sum_{n = 1}^{N/2} x_{2n+1}.e^{\frac{-2.i.\pi.k.n}{N/2}} $

$ \sum_{n = 1}^{N/4} x_{4n}.e^{\frac{-2.i.\pi.k.2n}{N/2}} + \sum_{n = 1}^{N/4} x_{4n + 2}.e^{\frac{-2.i.\pi.k.(2n + 1)}{N/2}} + e^{\frac{-2.i.\pi.k}{N}}.\left[\sum_{n = 1}^{N/4} x_{2(2n)+1}.e^{\frac{-2.i.\pi.k.2n}{N/2}} + \sum_{n = 1}^{N/4} x_{2(2n + 1) + 1}.e^{\frac{-2.i.\pi.k.(2n + 1)}{N/2}}\right]$


$ \sum_{n = 1}^{N/4} x_{4n}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N/2}}.\sum_{n = 1}^{N/4} x_{4n + 2}.e^{\frac{-2.i.\pi.k.2n}{N/2}} + e^{\frac{-2.i.\pi.k}{N}}.\left[\sum_{n = 1}^{N/4} x_{2(2n)+1}.e^{\frac{-2.i.\pi.k.2n}{N/2}} + \sum_{n = 1}^{N/4} x_{2(2n + 1) + 1}.e^{\frac{-2.i.\pi.k.(2n + 1)}{N/2}}\right]$

$ \sum_{n = 1}^{N/4} x_{4n}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N/2}}.\sum_{n = 1}^{N/4} x_{4n + 2}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N}}.\left[\sum_{n = 1}^{N/4} x_{4n+1}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N/2}}.\sum_{n = 1}^{N/4} x_{4n + 3}.e^{\frac{-2.i.\pi.k.2n}{N/2}}\right]$

$ \sum_{n = 1}^{N/4} x_{4n}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N/2}}.\sum_{n = 1}^{N/4} x_{4n + 2}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N}}.\left[\sum_{n = 1}^{N/4} x_{4n+1}.e^{\frac{-2.i.\pi.k.n}{N/4}} + e^{\frac{-2.i.\pi.k}{N/2}}.\sum_{n = 1}^{N/4} x_{4n + 3}.e^{\frac{-2.i.\pi.k.n}{N/4}}\right]$

$ \sum_{n = 1}^{N/8} x_{8n}.e^{\frac{-2.i.\pi.k.n}{N/8}} + $

$ e^{\frac{-2.i.\pi.k}{N/4}}.\sum_{n = 1}^{N/8} x_{8n + 4}.e^{\frac{-2.i.\pi.k.n}{N/8}} $ 

$+ e^{\frac{-2.i.\pi.k}{N/2}}\left[\sum_{n = 1}^{N/8} x_{8 + 2}.e^{\frac{-2.i.\pi.k.n}{N/8}} + e^{\frac{-2.i.\pi.k}{N/4}}.\sum_{n = 1}^{N/8} x_{8n + 6}.e^{\frac{-2.i.\pi.k.n}{N/8}}\right] $

$ + e^{\frac{-2.i.\pi.k}{N}}.[ \sum_{n = 1}^{N/8} x_{8n+1}.e^{\frac{-2.i.\pi.k.n}{N/8}} + e^{\frac{-2.i.\pi.k}{N/4}}.\sum_{n = 1}^{N/8} x_{8n+5}.e^{\frac{-2.i.\pi.k.n}{N/8}} + $

$ e^{\frac{-2.i.\pi.k}{N/2}}.(\sum_{n = 1}^{N/8} x_{8n + 3}.e^{\frac{-2.i.\pi.k.n}{N/8}} + e^{\frac{-2.i.\pi.k}{N/4}}.\sum_{n = 1}^{N/8} x_{8n + 7}.e^{\frac{-2.i.\pi.k.n}{N/8}})]$

__N = 8__
$ x_{0}.e^{\frac{-2.i.\pi.k.0}{N/8}} + $ 

$ e^{\frac{-2.i.\pi.k}{N/4}}(x_{4}.e^{\frac{-2.i.\pi.k.0}{N/8}}) $ 

$+ e^{\frac{-2.i.\pi.k}{N/2}}\left[x_{2}.e^{\frac{-2.i.\pi.k.0}{N/8}} + e^{\frac{-2.i.\pi.k}{N/4}}(x_{6}.e^{\frac{-2.i.\pi.k.0}{N/8}})\right] $

$ + e^{\frac{-2.i.\pi.k}{N}}.[x_{1}.e^{\frac{-2.i.\pi.k.0}{N/8}} + e^{\frac{-2.i.\pi.k}{N/4}}.(x_{5}.e^{\frac{-2.i.\pi.k.0}{N/8}}) + $

$ e^{\frac{-2.i.\pi.k}{N/2}}.(x_{3}.e^{\frac{-2.i.\pi.k.0}{N/8}} + e^{\frac{-2.i.\pi.k}{N/4}}(x_{7}.e^{\frac{-2.i.\pi.k.0}{N/8}}))]$

_Simplify_
__N = 8__
$ x_{0} + e^{\frac{-2.i.\pi.k}{2}}x_{4} + e^{\frac{-2.i.\pi.k}{4}}\left[x_{2} + e^{\frac{-2.i.\pi.k}{2}}x_{6}\right] + e^{\frac{-2.i.\pi.k}{8}}.[x_{1} + e^{\frac{-2.i.\pi.k}{2}}.x_{5} + e^{\frac{-2.i.\pi.k}{4}}.(x_{3} + e^{\frac{-2.i.\pi.k}{2}}x_{7})]$

$ [x_{0} + e^{\frac{-2.i.\pi.k}{2}} x_{4}][x_{2} + e^{\frac{-2.i.\pi.k}{2}}.x_{6}][x_{1} + e^{\frac{-2.i.\pi.k}{2}}.x_{5}][x_{3} + e^{\frac{-2.i.\pi.k}{2}}.x_{7}] = (A, B, C, D)_{k= 0, 1}$
 

$ A + e^{\frac{-2.i.\pi.k}{4}}\left[B\right] + e^{\frac{-2.i.\pi.k}{8}}.[C + e^{\frac{-2.i.\pi.k}{4}}.(D)]$

$ [A + e^{\frac{-2.i.\pi.k}{4}}B][C + e^{\frac{-2.i.\pi.k}{4}}D] = (E, F)_{k = 0, 1, 2, 3}$

$ E + e^{\frac{-2.i.\pi.k}{8}}F$

$ [E + e^{\frac{-2.i.\pi.k}{8}}F] = G_{k=0, 1, 2, 3, 4, 5, 6, 7} $

___pseudo code:___

$ [x_{0}, x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}, x_{7}] $
$ [x_{0}, x_{2}, x_{4}, x_{6}][x_{1}, x_{3}, x_{5}, x_{7}] $
$ [x_{0}, x_{4}][x_{2}, x_{6}][x_{1}, x_{5}][x_{3}, x_{7}] $

$ [x_{0}][x_{4}][x_{2}][x_{6}][x_{1}][x_{5}][x_{3}][x_{7}] $

$ [x_{0} + e_{0}.x_{4}][x_{2} + e_{0}.x_{6}][x_{1} + e_{0}.x_{5}][x_{3} + e_{0}.x_{7}] = [A, B, C, D]_{F=0} $

$ [x_{0} + e_{1}.x_{4}][x_{2} + e_{1}.x_{6}][x_{1} + e_{1}.x_{5}][x_{3} + e_{1}.x_{7}] = [A, B, C, D]_{F=1} $

$ [A_{0} + e_{0}.B_{0}][C_{0} + e_{0}.D_{0}] = [E, F]_{F=0} $
$ [A_{1} + e_{1}.B_{1}][C_{1} + e_{1}.D_{1}] = [E, F]_{F=1} $
$ [A_{0} + e_{2}.B_{0}][C_{0} + e_{2}.D_{0}] = [E, F]_{F=2} $
$ [A_{1} + e_{3}.B_{1}][C_{1} + e_{3}.D_{1}] = [E, F]_{F=3} $

$ [E_{0} + e_{0}.F_{0}] = G_{F=0} $
$ [E_{1} + e_{1}.F_{1}] = G_{F=1} $
$ [E_{2} + e_{2}.F_{2}] = G_{F=2} $
$ [E_{3} + e_{3}.F_{3}] = G_{F=3} $
$ [E_{0} + e_{4}.F_{0}] = G_{F=4} $
$ [E_{1} + e_{5}.F_{1}] = G_{F=5} $
$ [E_{2} + e_{6}.F_{2}] = G_{F=6} $
$ [E_{3} + e_{7}.F_{3}] = G_{F=7} $

lvls = 3  (0, 1, 2, 3)  // _lvl0 is the img_
nodes   = (8, 4, 2, 1)
fqLens  = (1, 2, 4, 8)  // _Frequencies_

(lvl, fq, nd)
lvl0 Size = 8
lvl1 Size = 8
lvl2 Size = 8
lvl3 Size = 8
fq0  Size = 1
fq1  Size = 2
fq2  Size = 4
fq3  Size = 8
(lvl * 8 + fq * nodes[lvl] + nd)

     0: lvl0,f0,0
     1: lvl0,f0,1
     2: lvl0,f0,2
     3: lvl0,f0,3
     4: lvl0,f0,4
     5: lvl0,f0,5
     6: lvl0,f0,6
     7: lvl0,f0,7

     8: lvl1,f0,0
     9: lvl1,f0,1
    10: lvl1,f0,2
    11: lvl1,f0,3
    12: lvl1,f1,0
    13: lvl1,f1,1
    14: lvl1,f1,2
    15: lvl1,f1,3

    16: lvl2,f0,0
    17: lvl2,f0,1
    18: lvl2,f1,0
    19: lvl2,f1,1
    20: lvl2,f2,0
    21: lvl2,f2,1
    22: lvl2,f3,0
    23: lvl2,f3,1

    24: lvl3,f0,0
    25: lvl3,f1,0
    26: lvl3,f2,0
    27: lvl3,f3,0
    28: lvl3,f4,0
    29: lvl3,f5,0
    30: lvl3,f6,0
    31: lvl3,f7,0

lvl * 8 + f*fqLen[lvl] nd

> fun ft(img)
ls[8 + 4.2 + 4.2 + 8.1] = 24
for nd in (0, nodes[0] / 2):
&nbsp;ls[0, 0, 2.nd] = img[nd]
&nbsp;ls[0, 0, 2.nd + 1] = img[4 + nd]
for lvl in (1, lvls):
&nbsp;node = nodes[lvl]
&nbsp;fqLen = fqLens[lvl]
&nbsp;for fq in (0, fqLen):
&nbsp;&nbsp;for nd in (0, nodes):
&nbsp;&nbsp;&nbsp;$ ls[lvl, fq, nd] = ls[lvl - 1,fq \% fqLens[lvl-1], 2.nd] + ls[lvl - 1, fq \% fqLens[lvl-1], 2.nd+1].e^{\frac{-2i\pi.fq}{fqLen}} $


---
##### FT applied to basic function (size = 8)
__lvl0__
$ [0][1][2][3][4][5][6][7] $

$ [0][4][2][6][1][5][3][7] $

__lvl1__
frequencies | real | imag
------------|------|-------
0           | 1    | 0
1           | -1   | 0
$ [0 + 4.e(1)][2 + 6.e(1)][1 + 5.e(1)][3 + 7.e(1)] = (A, B, C, D)_{F=0}$
$ [0 +4.e(-1)][2 +6.e(-1)][1 +5.e(-1)][3 +7.e(-1)] = (A, B, C, D)_{F=1}$

$ [ 4][ 8][ 6][10] = (A, B, C, D)_{F=0}$
$ [-4][-4][-4][-4] = (A, B, C, D)_{F=1} $

__lvl2__
frequencies | real | imag
------------|------|-------
0           | 1    | 0
1           | 0    | -1
2           | -1   | 0
3           | 0    | 1
$ [A + Be][C + D.e] = (E, F)_{F=0}$

$ [ 4 + 8.e(1) ][6 + 10.e(1) ] = (E, F)_{F=0}$
$ [-4 - 4.e(-i)][-4 - 4.e(-i)] = (E, F)_{F=1}$
$ [ 4 + 8.e(-1)][6 + 10.e(-1)] = (E, F)_{F=2}$
$ [-4 - 4.e(i) ][-4 - 4.e(i) ] = (E, F)_{F=3}$

$ [12          ][16          ] = (E, F)_{F=0}$
$ [-4 + 4i     ][-4 + 4i     ] = (E, F)_{F=1}$
$ [-4          ][-4          ] = (E, F)_{F=2}$
$ [-4 - 4i     ][-4 - 4i     ] = (E, F)_{F=3}$

__lvl3__

frequencies | real | imag
------------|------|-------
0           | 1    | 0
1           | 0.7  | -0.7
2           | 0    | -1
3           | -0.7 | -0.7
4           | -1   | 0
5           | -0.7 | 0.7
6           | 0    | 1
7           | 0.7  | 0.7

$ [E + F.e] = G_{F=0}$

$ [28] = G_{F=0}$

$ [-4 + 4i + e.(-4 + 4i)] = G_{F=1}$
$ [-4 + 4i + e(0.7 -0.7i)(-4 +4i)] = G_{F=1}$
$ [-4 + 4i + 5.6i] = G_{F=1}$
$ [-4 + 9.6i] = G_{F=1}$

$ [-4 + e(-4)] = G_{F=2}$
$ [-4 + e_{-i}(-4)] = G_{F=2}$
$ [-4 + 4i] = G_{F=2}$

$ [-4 - 4i + e.(-4 - 4i)] = G_{F=3}$
$ [-4 - 4i + e(-0.7 -0.7i)(-4 -4i)] = G_{F=3}$
$ [-4 - 4i + 5.6i] = G_{F=3}$
$ [-4 + 1.6i] = G_{F=3}$

$ [12 + e(16)] = G_{F=4}$
$ [12 - 16] = G_{F=4}$
$ [-4] = G_{F=4}$

$ [-4 + 4i + e.(-4 + 4i)] = G_{F=5}$
$ [-4 + 4i + e(-0.7 +0.7i)(-4 +4i)] = G_{F=5}$
$ [-4 + 4i - 5.6i] = G_{F=5}$
$ [-4 - 1.6i] = G_{F=5}$

$ [-4 + e(-4)] = G_{F=6}$
$ [-4 + e_{i}(-4)] = G_{F=6}$
$ [-4 - 4i] = G_{F=6}$

$ [-4 - 4i + e.(-4 - 4i)] = G_{F=7}$
$ [-4 - 4i + e(0.7 +0.7i)(-4 -4i)] = G_{F=7}$
$ [-4 - 4i - 5.6i] = G_{F=7}$
$ [-4 - 9.6i] = G_{F=7}$


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
&nbsp;&nbsp;
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
&nbsp;&nbsp;
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
&nbsp;&nbsp;
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