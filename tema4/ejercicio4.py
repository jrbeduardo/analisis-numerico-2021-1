## newtonPoly
import numpy as np
import sympy as sp
from sympy.plotting import plot
from math import *

x=sp.Symbol('x')

def difp(yData, iteracion=1, delta0=[]):
    if len(yData)>1:
        z=yData[:len(yData)-1]
        iteracion+=1
        delta=yData[1:len(yData)]-z
        delta0.append(round(delta[0],5))
        difp(delta, iteracion, delta0)
    return delta0

def factorial(k,n):
    product=1
    fact=1
    for i in range(n):
        product=(k-i)*product
        fact=(i+1)*fact
    return product/fact    

def polinomio_newton_simbolico(xData, yData, h):
    a=np.array(difp(yData, delta0=[]))
    k=(x-xData[0])/h
    resultado=yData[0]
    for i in range(len(a)):
        resultado=factorial(k,i+1)*a[i]+resultado
    return sp.expand(resultado)

def derivada_polinomio(xData, yData, h):
    pol=polinomio_newton_simbolico(xData, yData, h)
    return sp.diff(pol, x)

#extremos de los intervalos
a=0
b=1

#Tamaño de paso
h=0.1

#funcion propuesta

f=7*sp.exp(x)-2*(x**2)*sp.sin(2*x)-4*(x**3)-10

#derivada de f

derivada_original=sp.diff(f,x)

#datos para calcular el polinomio

xData=np.arange(a,b+h,h)

yData=7*np.exp(xData)-2*(xData**2)*np.sin(2*xData)-4*(xData**3)-10


derivada_pol=derivada_polinomio(xData, yData, h)

#graficas dela derivada  taylor y  la derivada original

p= plot(derivada_original, derivada_pol, (x, -2, 2), ylim=(-30, 40), show=False, legend=True)
p[0].line_color = 'k'
p[0].label = '$f^{\'}(x)$'
p[1].line_color = 'b'
p[1].label = '$p^{\'}(x)$'

p.show()

#Grafica del error absoluto

e1=abs(derivada_original-derivada_pol)

p1= plot(e1, (x, -1.5, 2), ylim=(-0.5, 2.5), show=False, legend=True)
p1[0].line_color = 'c'
p1[0].label = '$e_{a}(x)=|f^{\'}(x)-p^{\'}(x)|$'

p1.show()
