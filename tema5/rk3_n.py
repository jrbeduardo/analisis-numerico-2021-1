import numpy as np
import matplotlib.pyplot as plt

def run_kut3(f,t,x,h):
	K1 = np.round(h*f(t, x),3)
	K2 = np.round(h*f(t + 0.5*h, x + 0.5*K1),3)
	K3 = np.round(h*f(t + h, x - K1+2*k2),3)
	return  K1, K2, K3

def m_run_kut3(f,t,x,t_final,h):
	T=[t]
	X=[x]
	K1,K2, K3=[], [], []
	while t<=t_final:
		k1, k2, k3=run_kut2(f,t,x,h)
		x=np.round(x+(1/6.0)*(k1+4*k2+k3),3)
		t=round(t+h,3)
		if(t<=t_final):
			T.append(t)
			X.append(x)
		K1.append(k1)
		K2.append(k2)
		K3.append(k3)
	return np.array(T), np.matrix(X), K1, K2, K3

def f(t, x): return np.array([x[0]+2*x[1], 3*t*x[1]-np.sin(x[0])+t**2])

def f(t, x): return np.array([x[1], (1/5)*(x[0]**2)*x[1]*t+(2/5)*np.sin(t)])
#def mi_funcion(x): return 7*np.exp(x)-2*x**2*np.sin(x)-4*x**3-10

def datos_y(X,t):
	y=[] 
	for i in range(len(X)):
		y.append(7*X[i][0]-(2*t[i]**2)*X[i][1]-4*t[i]**3-10)
	return np.round(np.array(y),3) 


x0=np.array([1,2])
t,x,k1,k2=m_run_kut2(f,0,x0,0.6,0.2)


m=len(t)

print("\n\ni\t ti\t xi\t k1 \t k2\t error")
for i in range(m): print(f"{i}\t {t[i]}\t {x[i]} \t{k1[i]}\t{k2[i]}")




plt.plot(t,x[:,0])
plt.show()

#plt.plot(t,x[:,1])