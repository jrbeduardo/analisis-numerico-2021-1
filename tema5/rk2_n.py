import numpy as np
import matplotlib.pyplot as plt
import math

def round_well(num,p=0): return np.array([mi_round(mi_round(x,p+4),p) for x in num])

def round_well_num(num,p=0): return mi_round(mi_round(num,p+5),p)


def mi_round(num,p=0):
    expoN=num*10**p
    if abs(expoN)-abs(math.floor(expoN))<0.5:
        return math.floor(expoN)/10**p
    return math.ceil(expoN)/10**p


def run_kut2(f,t,x,h):
	K1 = round_well([h*m for m in f(t, x)],3)
	K2 = round_well([h*m for m in f(t + h, x + K1)],3)
	return  K1, K2

def m_run_kut2(f,t,x,t_final,h):
	T=[t]
	X=[x]
	K1,K2=[], []
	while t<=t_final:
		k1, k2=run_kut2(f,t,x,h)
		x=round_well(x+(1/2.0)*(k1+k2),3)
		t=round_well_num(t+h,3)
		if(t<=t_final):
			T.append(t)
			X.append(x)
		K1.append(k1)
		K2.append(k2)
	return np.array(T), np.matrix(X), K1, K2


def f(t, x): return np.array([ x[1], x[2], (1/(3*t))*(np.exp(-t)*x[2]+x[1]+np.sin(t)*x[0]-4*np.cos(t*x[0]))])

#def f(t, x): return np.array([x[0]+2*x[1], 3*t*x[1]-np.sin(x[0])+t**2])
#def f(t, x): return [ round_well_num(x[1],3), round_well_num( (1/5)*(x[0]**2)*x[1]*t+(2/5)*math.sin(t), 3)]


#def mi_funcion(x): return 7*np.exp(x)-2*x**2*np.sin(x)-4*x**3-10

def datos_y(X,t):
	y=[] 
	for i in range(len(X)):
		y.append(7*X[i][0]-(2*t[i]**2)*X[i][1]-4*t[i]**3-10)
	return round_well(np.array(y),3) 


x0=np.array([2,0,0])
t,x,k1,k2=m_run_kut2(f,1,x0,1.5,0.25)


m=len(t)

print("\n\ni\t ti\t xi\t k1 \t k2\t error")
for i in range(m): print(f"{i}\t {t[i]}\t {x[i]} \t{k1[i]}\t{k2[i]}")


'''

plt.plot(t,x[:,0])
plt.show()
'''
#plt.plot(t,x[:,1])