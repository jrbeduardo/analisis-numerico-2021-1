#ejemplos
import numpy as np
from tema2 import *

#A=np.matrix([[2,2,3],[-10,1,2], [-2,4,9]])
#x=np.matrix([[-22],[-34], [-62]])
#print(A)
#print(x)
#print(np.dot(A,x))
a=np.matrix([[4,-1,1], [1,3,-1],[1,1,7]])
#a=np.matrix([[1, -1, -2], [-4, 0, 3], [-4, -2, 8]])

l,u=LUdecomp(a)
print('-----------------------')
print('DOOLITTLE')
print('-----------L-----------')
print(l)
print('-----------U-----------')
print(u)
print('-----------LU-----------')
print(np.dot(l,u))

'''
l,u=crout(a)
print('-----------------------')

print('CROUT')
print('-----------L-----------')
print(l)
print('-----------U-----------')
print(u)
print('-----------LU-----------')
print(np.dot(l,u))
'''


'''
def miround(x): return round(round(x,7),3)

def iterEqs(y):
	x =[0.000, 0.000, 0.000]
	x[0]=miround(1/6*(18-3*y[1]-2*y[2]))
	x[1]=miround(1/6*(23-2*y[0]-3*y[2]))
	x[2]=miround(-1/7*(-11-2*y[0]-4*y[1]))
	return x

def iterEqs1(x):
	x[0]=miround(1/6*(18-3*x[1]-2*x[2]))
	x[1]=miround(1/6*(23-2*x[0]-3*x[2]))
	x[2]=miround(-1/7*(-11-2*x[0]-4*x[1]))
	return x

n = 3
x =[0.0, 0.0, 0.0]
x,numIter= jacobi(iterEqs,x)
print("\nNumero de iteraciones =",numIter)
print("\nLa solución es:\n",x)
print(round(2.7145,3))'''