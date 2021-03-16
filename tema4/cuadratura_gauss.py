'''x,A = gaussNodosPesos(m)
Devuelve los nodos {x} y la lista de pesos {A} para un polinomio de legendre de grado m
'''

import math
import numpy as np

def gaussNodosPesos(m):
	if m==1:
		x=np.array([0])
		W=np.array([2])
		return x,W
	elif m==2:
		x=np.array([np.sqrt(1/3),-np.sqrt(1/3)])
		W=np.array([1,1])
		return x,W
	elif m==3:
		x=np.array([0,np.sqrt(3/5),-np.sqrt(3/5)])
		W=np.array([8/9, 5/9, 5/9])
		return x,W
	elif m==4:
		x=np.array([np.sqrt((3-2*np.sqrt(6/5))/7), -np.sqrt((3-2*np.sqrt(6/5))/7), np.sqrt((3+2*np.sqrt(6/5))/7),-np.sqrt((3+2*np.sqrt(6/5))/7)])
		W=np.array([(18+np.sqrt(30))/36, (18+np.sqrt(30))/36, (18-np.sqrt(30))/36,(18-np.sqrt(30))/36])
		return x,W
	elif m==5:
		x=np.array([0,(1/3)*np.sqrt(5-2*np.sqrt(10/7)), -(1/3)*np.sqrt(5-2*np.sqrt(10/7)), (1/3)*np.sqrt(5+2*np.sqrt(10/7)),-(1/3)*np.sqrt(5+2*np.sqrt(10/7))])
		W=np.array([128/225,(322+13*np.sqrt(70))/900, (322+13*np.sqrt(70))/900, (322-13*np.sqrt(70))/900,(322-13*np.sqrt(70))/900])
		return x,W
	else:
		print('no se tienen la lista de nodos y pesos para el valor {}'.format(m))
		return

def gaussQuad(f,a,b,m):
	c1 =(b + a)/2.0
	c2 = (b - a)/2.0
	x,A = gaussNodosPesos(m)
	sum = 0.0
	for i in range(len(x)):
		print(round(c1 + c2*x[i],5))
		sum = sum + round(A[i],3)*f(round(c1 + c2*x[i],5))
	return c2*sum

def f(x): return (1/np.sqrt(np.pi*2))*np.exp(-.5*x**2)
def g(x): return x*np.log(x)
def h(x): return np.exp(np.cos(x))

a=-3
b=3
n=5
x,A=gaussNodosPesos(5)

c=1/np.sqrt(np.pi*2)

#print('alpha={}'.format((b - a)/2.0))
#print('betha={}'.format((b + a)/2.0))

print('Nodos xi: {}'.format(np.round(x,5)))

print('Pesos wi: {}'.format(np.round(A,5)))

print((gaussQuad(f,-3,-0.6, 2)+gaussQuad(f,-0.6,3, 3)))


