from tema2 import *
import numpy as np

'''PROYECTO
aproxime alguna de las raıces de su funcion, utilizando biseccion, regla falsa y Newton-
Raphson con un error (porcentual) menor a 1x10^-10, indique claramente cuales son los valores
[a,b] y x0 empleados en cada metodo. Ası mismo, explique cual fue el mejor y cual fue el
peor algoritmo para resolver el problema
'''

#funcion propuesta

def f(x): return 7*np.exp(x)-2*(x**2)*np.sin(2*x)-4*(x**3)-10

#Derivada de la funcion propuesta

def derivada(x): return 7*np.exp(x)-4*x*np.sin(2*x)-4*(x**2)*np.cos(2*x)-12*(x**2)

#función requerida para el metodo del punto fijo

def g(x): return np.log( (1/7)*(2*(x**2)*np.sin(2*x)+4*(x**3)+10) )

#intervalo

a=0
b=1
x0=0.5

#metodos para aproximar la raiz en el intervalo [a,b] elegidos

bisection(f,a,b)

regla_falsa(f,a,b)

punto_fijo(g,x0)

newton_rapson(f, derivada, x0)