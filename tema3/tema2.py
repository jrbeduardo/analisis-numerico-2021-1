#tema2
## Doolittle
''' a = LUdecomp(a)
PASO 1.  [L][U] = [a]
x = LUsolve(a,b)
PASO 2.  [L][U]{x} = {b}
'''
import numpy as np
import math

def LUdecomp(A):
	n = len(A)
	U = np.zeros((n,n))
	L = np.zeros((n,n))
	for k in range(n):
		U[0,k]=round(A[0,k],3)
		L[k,0]=round(A[k,0]/U[0,0],3)
	for i in range(1,n-1):
		for j in range(i,n):
			s1=0
			for k in range(i):
				s1+=L[i,k]*U[k,j]
			s1=round(s1,3)
			U[i,j]=A[i,j]-s1
		for t in range(i,n):
			s2 = sum(L[t,k]*U[k,i] for k in range(i))
			L[t,i] =round((A[t,i]-s2)/U[i,i],3)
	sn= sum(L[n-1,k]*U[k,n-1] for k in range(n-1))
	U[n-1,n-1]=round(A[n-1,n-1]-sn,3)
	L[n-1, n-1]=1.0
	return L, U

def LUsolve(a,b):
	n = len(a)
	for k in range(1,n):
		b[k] = b[k] - np.dot(a[k,0:k],b[0:k])
	b[n-1] = b[n-1]/a[n-1,n-1]
	for k in range(n-2,-1,-1):
		b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
	return b

def crout(A):
    L = np.zeros((3, 3))
    U = np.zeros((3, 3))
    for k in range(0, 3):
        U[k,k] = 1 
        for j in range(k, 3):
            sum0 = sum([L[j, s]*U[s, k] for s in range(0, j)]) #range from index 0
            L[j, k] = round(A[j, k] - sum0,3) #reversed index

        for j in range(k+1, 3):
            sum1 = sum([L[k, s] * U[s, j] for s in range(0, k)]) #range from index 0
            U[k, j] = round((A[k, j]-sum1)/ L[k, k],3)
    return L, U

def jacobi(iterEqs, x, tol=0.01):
	print('{}	{}	{}	{}	{}'.format('i', 'x1', 'x2', 'x3', 'e'))
	for i in range(1,1000):
		xold = x.copy()
		x = iterEqs(x)
		dx = round(math.sqrt((x[0]-xold[0])**2+(x[1]-xold[1])**2+(x[2]-xold[2])**2),3)
		print('{}	{}	{}	{}	{}'.format(i, x[0], x[1], x[2], dx))
		if dx<tol: return x,i
	print('Jacobi no converge')
