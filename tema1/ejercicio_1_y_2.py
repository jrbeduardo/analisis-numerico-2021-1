'''
1. Proponga una función trascendente, la cual esté formada por la combinación de funciones
trigonométricas, exponenciales y algebraicas. Grafique
f(x) en algun dominio en el que no presente discontinuidades, y en el cual posea una o mas raıces,
indicando claramente el intervalo [a, b].

2. Aproxime su funcion con la serie de Taylor y grafique los polinomios p5(x), p10(x) y
p100(x), ası como las graficas de los errores absolutos con respecto a la funcióon original (en el caso
de p100(x) el error deberıa ser casi nulo). Proporcione una explicacion de que
ocurre cuando se incrementa el numero de terminos de la serie.
'''
import numpy as np
import sympy as sp
from sympy.plotting import plot
from math import *

x=sp.Symbol('x')

#funcion que calcula el polinomio de taylor de grado cualquiera alrededor de un punto x0

def polinomio_symbolico(f, grado, x0=0):
	suma=f.subs(x,x0)
	for i in range(1, grado+1):
		derivada=sp.diff(f,x,i)
		suma=suma+(derivada.subs(x,x0)/factorial(i))*(x-x0)**i 
	return  sp.expand(suma)

#funcion propuesta

f=7*sp.exp(x)-2*(x**2)*sp.sin(2*x)-4*(x**3)-10

#grafica de la funcion

plot(f, (x, -6, 6), ylim=(-20, 100), label='$f(x)=7e^x-2x^2\\sin(2x)-4x^3-10$', legend=True)

#Calculo de los polinomio de taylor que se piden alrededor de x0=0

t5=polinomio_symbolico(f, 5, 0)

t10=polinomio_symbolico(f, 10, 0)

t100=polinomio_symbolico(f, 100, 0)

#graficas de los polinomios y la funcion propuesta

p= plot(f, t5, t10, t100, (x, -6, 6), ylim=(-20, 100), show=False, legend=True)
p[0].line_color = 'k'
p[0].label = '$f(x)$'
p[1].line_color = 'b'
p[1].label = '$p_{5}(x)$'
p[2].line_color = 'c'
p[2].label = '$p_{10}(x)$'
p[3].line_color = 'red'
p[3].label = '$p_{100}(x)$'

p.show()

#Grafica de los del errores absolutos
e1=abs(f-t5)
e2=abs(f-t10)
e3=abs(f-t100)

p1= plot(e1, e2, e3, (x, -20, 20), ylim=(-1, 30), show=False, legend=True)
p1[0].line_color = 'b'
p1[0].label = '$e_{1}(x)=|f(x)-p_{5}(x)|$'
p1[1].line_color = 'c'
p1[1].label = '$e_{2}(x)=|f(x)-p_{10}(x)|$'
p1[2].line_color = 'red'
p1[2].label = '$e_{3}(x)=|f(x)-p_{100}(x)|$'

p1.show()
