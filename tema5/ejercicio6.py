import numpy as np
import matplotlib.pyplot as plt

def run_kut4(f,t,x,h):
	K1 = np.round(h*f(t, x),3)
	print(K1)
	K2 = np.round(h*f(t + h/2.0, x + K1/2.0),3)
	K3 = np.round(h*f(t + h/2.0, x + K2/2.0),3)
	K4 = np.round(h*f(t + h, x+K3),3)
	return  K1, K2, K3, K4

def m_run_kut4(f,t,x,t_final,h):
	T=[t]
	X=[x]
	K1,K2,K3, K4=[], [], [], []
	while t<=t_final:
		k1, k2, k3, k4=run_kut4(f,t,x,h)
		x=np.round(x+(1/6.0)*(k1+2*k2+2*k3+k4),3)
		t=round(t+h,3)
		T.append(t)
		K1.append(k1)
		K2.append(k2)				
		K3.append(k3)
		K4.append(k4)
		X.append(x)
	return np.array(T), X, K1, K2, K3, K4

def f(t, x): return np.array([x[0], 2*x[2], -4*x[1]])

def datos_y(X,t):
	y=[] 
	for i in range(len(X)):
		y.append(2*X[i][0]-2*t[i]**2*X[i][1]-4*t[i]**3-10)
	return np.round(np.array(y),3) 


x0=np.array([1,0,1])
t,x,k1,k2,k3,k4=m_run_kut4(f,0,x0,1,0.1)

m=min(len(t),len(x),len(k1))

print("\n\ni\t xi\t yi\t k1 \t k2\t k3 \t k4\t error")
for i in range(m): print(f"{i}\t {t[i]}\t {x[i]} \t{k1[i]}\t{k2[i]}\t{k3[i]}\t{k4[i]}")

yData=datos_y(x,t)

plt.plot(t,yData, 'bo')

