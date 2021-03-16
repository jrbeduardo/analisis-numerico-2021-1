## module newtonPoly
import numpy as np
import sympy as sp

x=sp.Symbol('x')


def difp(yData, iteracion=1, delta0=[]):
    if len(yData)>1:
        z=yData[:len(yData)-1]
        iteracion+=1
        delta=yData[1:len(yData)]-z
        delta0.append(round(delta[0],5))
        print(delta)
        difp(delta, iteracion, delta0)
    return delta0

def factorial(k,n):
    product=1
    fact=1
    for i in range(n):
        product=(k-i)*product
        fact=(i+1)*fact
    return product/fact    

def polinomio_newton_numerico(xData, yData, t, h):
    a=np.array(difp(yData,delta0=[]))
    k=(t-xData[0])/h
    resultado=yData[0]
    for i in range(0,len(a)):
        resultado=factorial(k,i+1)*a[i]+resultado
    return resultado

def polinomio_newton_simbolico(xData, yData, h):
    a=np.array(difp(yData, delta0=[]))
    k=(x-xData[0])/h
    resultado=yData[0]
    for i in range(len(a)):
        resultado=factorial(k,i+1)*a[i]+resultado
    return sp.expand(resultado)


'''
#x=[0.2,0.4,0.6,0.8]
y=[ 0.832, .867, 1, 1.3]
#xData = np.array(x)
xData=np.arange(0.6,1.2,0.2)
yData = np.array(y)


f=sp.exp(sp.ln(x)*(x**2))
f_1=sp.diff(f,x)
f_2=sp.diff(f_1,x)
print(f_1)
print(f_2)



#print(polinomio_newton_numerico(xData,yData, 1.75,0.2))
polinomio_newton=polinomio_newton_simbolico(xData,yData, 0.2)
derivada_1=sp.diff(polinomio_newton,x)
derivada_2=sp.diff(derivada_1,x)
print(derivada_2)

print(derivada_2.subs(x,1.1))
'''