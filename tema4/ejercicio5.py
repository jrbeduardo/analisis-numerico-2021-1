from cuadratura_gauss import *
from newton_cotes import *
import numpy as np

'''Integre la función en el intervalo [a; b] utilizando todos los métodos de integración numérica
correctamente: trapecial, S. 1/3, S. 3/8 con n = 600 y cuadratura gaussiana (con polinomios de
Legendre de grados 2, 3 y 4); para cada caso, calcule el error absoluto. ¿Cual fue el mejor método?
'''

#funcion propuesta

def f(x): return 7*np.exp(x)-2*(x**2)*np.sin(2*x)-4*(x**3)-10

#intervalo

a=0
b=1

#valor real de la integral

I= (1/2)*(-35 + 14*np.exp(1) - 2*np.sin(2) + np.cos(2))

print('----------Valor de la Integral------------')
print(I)

print('----------Newton-Cotes------------')
trapecial=trapecial(f,0,1,6)
simpson13=simpson13(f,0,1,6)
simpson38=simpson38(f,0,1,6)


print('Trapecial: {}, error: {}'.format(trapecial, abs(trapecial-I)))
print('Simpson 1/3: {}, error: {}'.format(simpson13, abs(simpson13-I)))
print('Simpson 3/8: {}, error: {}'.format(simpson38, abs(simpson38-I)))

errores={'trapecial':abs(trapecial-I), 'simpson 1/3':abs(simpson13-I), 'simpson 3/8':abs(simpson38-I)}


print('----------Cuadratura de Gauss------------')

for i in range(2,6):
	cuadratura=gaussQuad(f,0,1,i)
	errores['Polinomio de Legendre de grado '+str(i)]=abs(cuadratura-I)
	print('Polinomio de Legendre de grado {}: {}, error: {}'.format(i,cuadratura, abs(cuadratura-I)))

for metodo in errores:
	if errores[metodo]==min(errores.values()):
		print('----------------------------------------')
		print('El mejor metodo es '+metodo)
		break