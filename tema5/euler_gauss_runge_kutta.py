import numpy as np
import math
import decimal 

def round_well(num,p):
    return float(decimal.Decimal(num).quantize(decimal.Decimal('.001'), rounding=ROUND_HALF_UP))

Dado que una relación es un conjunto (o una bolsa), no hay un orden definido para una relación. Es decir, dos relaciones son iguales si contienen las mismas tuplas, independientemente del orden.

def m_euler(f, x0, y0, h, n):
	x=[x0]
	y=[y0]
	for i in range(n):
		x.append(round_well(x[i]+h,3))
		y.append(round_well(y[i]+h*f(x[i], y[i]),3))
	X, Y=np.array(x), np.array(y)
	return X, Y

def m_euler_gauss(f, x0, y0, h, n):
	x=[x0]
	y=[y0]
	yE=[0]
	for i in range(n):
		x_next=round_well(x[i]+h,3)
		p=round_well(y[i]+h*f(x[i], y[i]),3)
		yE.append(round_well(y[i]+h*f(x[i], y[i]),3))
		x.append(x_next)
		y.append(round_well(y[i]+(h/2)*(f(x[i], y[i])+f(x_next, p)),3))
	X, Y, Z=np.array(x), np.array(y), np.array(yE)
	return X, Y,Z
 


def run_kut3(f,x,y,h):
	K1 = round_well(h*f(x, y),3)
	K2 = round_well(round_well(h*f(x + h/2.0, y + K1/2.0), 9),3)
	K3 = round_well(h*f(x + h, y - K1 + 2.0*K2),3)
	return  K1, K2, K3

def m_run_kut3(f,x,y, x_final,h):
	X=[x]
	Y=[y]
	K1,K2,K3=[], [], []
	while x<=x_final:
		k1,k2,k3=run_kut3(f,x,y,h)
		y=round_well(y+(1/6.0)*(k1+4*k2+k3),3)
		x=round_well(x+h,3)
		K1.append(k1)
		K2.append(k2)				
		K3.append(k3)
		X.append(x)
		Y.append(y)
	return np.array(X),np.array(Y), np.array(K1), np.array(K2), np.array(K3)

def run_kut4(f,x,y,h):
	K1 = round_well(h*f(x, y),3)
	K2 = round_well(round_well(h*f(x + h/2.0, y + K1/2.0), 9),3)
	K3 = round_well(h*f(x + h/2.0, y + K2/2.0),3)
	K4 = round_well(h*f(x + h, y+K3),3)
	return  K1, K2, K3, K4

def m_run_kut4(f,x,y, x_final,h):
	X=[x]
	Y=[y]
	K1,K2,K3, K4=[], [], [], []
	while x<=x_final:
		k1,k2,k3, k4=run_kut4(f,x,y,h)
		y=round_well(y+(1/6.0)*(k1+2*k2+2*k3+k4),3)
		x=round_well(x+h,3)
		K1.append(k1)
		K2.append(k2)				
		K3.append(k3)
		K4.append(k4)
		X.append(x)
		Y.append(y)
	return np.array(X),np.array(Y), np.array(K1), np.array(K2), np.array(K3), np.array(K4)


#--------------------------------------------------------

def f(x,y): return x+2*x*y



x,y=m_euler(f, 0.5, 1, 0.1,5)

solucion=np.round_well(2*np.exp(np.sin(x)),3)

print("i\t xi\t yi")
for i in range(len(x)): print(f"{i}\t {x[i]}\t {y[i]} \t {solucion[i]}\t {abs(solucion[i]-y[i])}")


x,y, ye=m_euler_gauss(f, 0, 2, 0.5,5)
print("\n\ni\t xi\t yi\t y_e")
for i in range(len(x)): print(f"{i}\t {x[i]}\t {y[i]} \t{ye[i]}\t {abs(solucion[i]-y[i])}")



x,y,k1,k2,k3=m_run_kut3(f, 1, 3, 2.5 ,0.5)

m=min(len(x),len(y),len(k1))

print("\n\ni\t xi\t yi\t k1 \t k2\t k3\t error")
for i in range(m): print(f"{i}\t {x[i]}\t {y[i]} \t{k1[i]}\t{k2[i]}\t{k3[i]}\t {abs(solucion[i]-y[i])}")



x,y,k1,k2,k3, k4=m_run_kut4(f, 1, 3, 2.5 ,0.5)

m=min(len(x),len(y),len(k1))

print("\n\ni\t xi\t yi\t k1 \t k2\t k3 \t k4\t error")
for i in range(m): print(f"{i}\t {x[i]}\t {y[i]} \t{k1[i]}\t{k2[i]}\t{k3[i]}\t{k4[i]}\t {abs(solucion[i]-y[i])}")

