import numpy as np
from math import *
from  pol_newton import *

def f(t): return round(log(t+9)+2,5) 

def richardson(D1, D2, h1, h2):
	return D2+(1/((h1/h2)**2-1))*(D2-D1)



xi=np.array([3,5,7])
yi=np.array([f(t) for t in xi])

print(yi)


h1=2
h2=1

poly_newton=polinomio_newton_simbolico(xi,yi, 2)

derivada_1=sp.diff(poly_newton,x)

D1=derivada_1.subs(x,5)

print(f"D1={D1}")


xi=np.array([4,5,6])
yi=np.array([f(t) for t in xi])

print(yi)

poly_newton=polinomio_newton_simbolico(xi,yi, 1)

derivada_1=sp.diff(poly_newton,x)

D2=derivada_1.subs(x,5)

print(f"D2={D2}")

print('Richardson={}'.format(richardson(D1,D2, h1,h2)))


