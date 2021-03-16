#ejemplos
import numpy as np
import math
from tema2 import *

def potencias_max(A, x0, lamda_anterior=0, tol=0.1, iter=1):
	x_prod=np.round(np.dot(A,x0),3)
	lamda=x_prod[np.argmax(np.abs(x_prod))]
	x=np.round(x_prod/lamda,3)
	print('{}	{}	{}	{}'.format(iter, x_prod,x,lamda, x))
	#if abs(lamda-lamda_anterior)<tol: 
	if iter==10:
		print('FIN')
	else:
		iter=iter+1
		potencias_max(A, x, lamda_anterior=lamda,iter=iter)

def potencias_min(B, x0, lamda_anterior=0, tol=0.1, iter=1):
	x_prod=np.round(np.dot(B,x0),3)
	lamda_inversa=x_prod[np.argmax(np.abs(x_prod))]
	x=np.round(x_prod/lamda_inversa,3)
	lamda=round(1/lamda_inversa,3)
	print('{}	{}	{}	{}'.format(iter, x_prod, x, lamda))
	#if abs(lamda-lamda_anterior)<tol: 
	if iter==10:
		print('FIN')
	else:
		potencias_min(B, x, lamda_anterior=lamda,iter=iter+1)


A=np.array([[4.0,-1.0, 1.0],[1.0,3.0,-1.0], [1,1,7]])
print('iter		vector_prod 	vector_propio 	lamda')
potencias_max(A,[1,0,0])
#A_inversa=np.array([[-0.5,-1,1],[0.1,0,.2], [-1.4,-2,2.2]])
#potencias_min(A_inversa,[1,0,0])

#a=np.matrix([[2,4,1,-3], [-1,-2,2,4],[4,2,-3,5],[5,-4,-3,1]])

#a=np.matrix([[1, -1, -2], [-4, 0, 3], [-4, -2, 8]])

'''l,u=crout(a)

print(np.dot(l,u))'''

