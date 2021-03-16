## Tema 2 Raices de ecuaciones
'''
-------------Metodos cerrrados----------
1. biseccion
2. Regla Falsa
------------Metodos abiertos------------
1. Punto fijo
2. Newton Rahpson
3. Metodo de Lin
'''
import math
from numpy import *

#cifras decimales 

def error(v_real, v_aprox): return math.abs(v_real-v_aprox)/v_real

def bisection(f,x1,x2,tol=1e-10):
	print('-----------------\nBiseccion\n----------------')
	f1 = round(f(x1),3)
	if f1 == 0.0: return x1
	f2 = round(f(x2),3)

	if f2 == 0.0: return x2
	if sign(f1) == sign(f2):
		print('La función no tiene raíces en este intervalo')
		return None
	x3=0
	while abs(x2-x1)/x2>=tol:
		x3 = 0.5*(x1 + x2); f3 = f(x3)
		if f3 == 0.0: return x3
		if sign(f2)!= sign(f3): x1 = x3; f1 = f3
		else: x2 = x3; f2 = f3
	print(x3)


def regla_falsa(f,x1,x2, tol=1e-10):
	print('-----------------\nRegla Falsa\n----------------')
	f1 = f(x1)
	if f1 == 0.0: return x1
	f2 = f(x2)
	if f2 == 0.0: return x2
	if sign(f1) == sign(f2):
		print('La función no tiene raíces en este intervalo')
		return None
	x3=0
	while abs(x2-x1)/x2>=tol:
		x3 = x2-f(x2)*(x2 -x1)/(f(x2)-f(x1)) 
		f3 =f(x3)
		if sign(f2)!= sign(f3): 
			x1 = x3 
			f1 = f3
		else: 
			x2 = x3 
			f2 = f3
	print(x3)

def punto_fijo(g, inicio, tol=1e-10):
	print('-----------------\nPunto fjo\n----------------')
	siguiente=g(inicio)
	actual=inicio
	error=abs(actual-siguiente)/siguiente
	while( error>=tol):
		error=abs(actual-siguiente)/siguiente
		actual=siguiente
		siguiente=g(siguiente)
	print(siguiente) 
	
def newton_rapson(funcion, derivada, inicio, tol=1e-10):
	print('-----------------\nNewton-Raphson\n----------------')
	siguiente=inicio-funcion(inicio)/derivada(inicio)
	actual=inicio
	error=abs(actual-siguiente)/siguiente
	while( error>=tol):
		error=abs(actual-siguiente)/siguiente
		actual=siguiente
		siguiente=siguiente-funcion(siguiente)/derivada(siguiente)
	print(siguiente)


def metodo_lin(a, redondeo=3):
	n=len(a)-1
	#Condiciones iniciales
	p=[0]; q=[0]
	incremento_p=[round(a[n-1]/a[n-2], redondeo)]
	incremento_q=[round(a[n]/a[n-2], redondeo)]
	#ecuaciones de recurrencia
	print('i={}'.format(0))		
	print('{} {} {} {} {} '.format(p[0], q[0],a, incremento_p[0], incremento_q[0] ))

	for i in range(1,7):
		p.append(round(p[len(p)-1]+incremento_p[len(p)-1],redondeo))
		q.append(round(q[len(q)-1]+incremento_q[len(q)-1],redondeo))
		b=coeficientes(p[i],q[i],a, redondeo)
		r, s, e = CalculoR_S(a, b, p[i],q[i], redondeo)
		incremento_p.append(round(r/b[n-2],redondeo))
		incremento_q.append(round(s/b[n-2],redondeo))
		print('\n------------------------------------------------------------------------------------\ni={}'.format(i))
		
		print('p={} q={} b={} R={} S={} Ip={} Iq={} e={}'.format(p[i], q[i],b, r,s, incremento_p[i], incremento_q[i], e))



def coeficientes(pi, qi, a, redondeo):
		b=[]
		for k in range(len(a)-2):
			if k==0:
				b.append(a[0])
			elif k==1: 
				b.append(round(a[1]-pi*b[0],redondeo))
			else:
				b.append(round(a[k]-pi*b[k-1]-qi*b[k-2],redondeo))
		return b

def CalculoR_S(a, b, pi, qi, redondeo):
	n=len(a)-1
	R=round(a[n-1]-pi*b[n-2]-qi*b[n-3],redondeo)
	S=round(a[n]-qi*b[n-2], redondeo)
	return R, S, round(math.sqrt(R*R+S*S),redondeo)