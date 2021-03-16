import sympy as sp
from math import factorial

x=sp.Symbol('x')
sp.init_printing()

def comb(m, n): return factorial(m)/(factorial(n) * factorial(m - n))

def pol_legendre(n):
	legendre=(x+1)**n
	for k in range(1,n+1):
		legendre=legendre+(comb(n,k)**2)*((x+1)**(n-k))*((x-1)**k)
	#legendre=(1/2**n)*legendre
	return sp.expand(legendre)

for i in range(1,11):
	sp.pprint(pol_legendre(i))