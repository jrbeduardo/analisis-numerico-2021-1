#interpolacion de Lagrange
#http://pyciencia.blogspot.com/2017/04/interpolacion-de-lagrange.html
import sympy as sp
import numpy as np

def interpolacion_lagrage_numerica(x, y, t):
    points=len(x)
    lj = []
    for k in range(points):
        lk =1
        for s in range(points):
            if s!=k:
                lk=lk*(t-x[s])/(x[k]-x[s])
        lj.append(lk)
    return sum(y*lj)

def interpolacion_lagrage_simb(xData, yData):
    n=len(xData)
    x=sp.Symbol('x')
    lj = []
    for k in range(n):
        lk =1
        for s in range(n):
            if s!=k:
                lk=lk*(x-xData[s])/(xData[k]-xData[s])
        lj.append(lk)
    return sp.expand(sum(yData*lj))



# Datos 


x = np.array([1.0,1.5,2.0])
y = np.array([1.81636,0.58773,-0.56162])

t=1.75
print('f_{}({})={}'.format(len(x)-1,t, interpolacion_lagrage_numerica(x,y,t)))
print(interpolacion_lagrage_simb(x,y))

# Gráfica
'''
plt.plot(x_test, y_pol)
plt.scatter(x, y)
plt.legend(['Lagrange', 'Datos'], loc='best')
plt.show()'''