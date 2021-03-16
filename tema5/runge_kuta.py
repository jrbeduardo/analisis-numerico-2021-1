## module run_kut4
''' X,Y = integrate(F,x,y,xStop,h).
4th-order Runge-Kutta method for solving the
initial value problem {y}' = {F(x,{y})}, where
{y} = {y[0],y[1],...y[n-1]}.
x,y = initial conditions
xStop = terminal value of x
h = increment of x used in integration
F = user-supplied function that returns the
array F(x,y) = {y'[0],y'[1],...,y'[n-1]}.
'''
import numpy as np
import matplotlib.pyplot as plt

def run_kut4(F,x,y,h):
	K0 = h*F(x,y)
	K1 = h*F(x + h/2.0, y + K0/2.0)
	K2 = h*F(x + h/2.0, y + K1/2.0)
	K3 = h*F(x + h, y + K2)
	return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0

def integrate(F,x,y,xStop,h):
	X = []
	Y = []
	X.append(x)
	Y.append(y)
	while x < xStop:
		h = min(h,xStop - x)
		y = y + run_kut4(F,x,y,h)
		x = x + h
		X.append(x)
		Y.append(y)
	return np.array(X),np.array(Y)

def printSoln(X,Y,freq):
	def printHead(n):
		print("\n x ",end=" ")
		for i in range (n):
			print(" y[",i,"] ",end=" ")
		print()
		
	def printLine(x,y,n):
		print("{:13.4e}".format(x),end=" ")
		for i in range (n):
			print("{:13.4e}".format(y[i]),end=" ")
		print()
	m = len(Y)
	try: n = len(Y[0])
	except TypeError: n = 1
	if freq == 0: freq = m
	printHead(n)
	for i in range(0,m,freq):
		printLine(X[i],Y[i],n)
	if i != m - 1: printLine(X[m - 1],Y[m - 1],n)

def F(x,y):
	F = np.zeros(2)
	F[0] = y[1]
	F[1] = -0.1*y[1] - x
	return F


x = 0.0 # Start of integration
xStop = 2.0 # End of integration
y = np.array([0.0, 1.0]) # Initial values of {y}
h = 0.05 # Step size
X,Y = integrate(F,x,y,xStop,h)
yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)
freq=20
plt.plot(X,Y[:,0],'o',X,yExact,'-')
plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('Numerical','Exact'),loc=0)
plt.show()
printSoln(X,Y,freq)
input("Press return to exit")
