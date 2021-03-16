import numpy as np

def trapecial(f, x0, xn, n):
	xData=np.linspace(x0, xn, num=n+1)
	h=(xn-x0)/n
	yData=np.round(f(xData),5)
	if n==0:
		print('no se puede aplicar este metodo pues n=0')
		return 
	else:
		imprimir_datos(xData, yData)		
		return (h/2)*(yData[0]+yData[n]+2*np.sum(yData[1:n]))

def simpson13(f, x0, xn, n):
	xData=np.linspace(x0, xn, num=n+1)
	h=(xn-x0)/n
	yData=np.round(f(xData),5)
	if n%2!=0:
		print('no se puede aplicar este metodo pues n no es par')
		return 
	else:
		imprimir_datos(xData, yData)
		suma_par=0
		suma_impar=0
		for i in range(1,n):
			if i%2==0:
				suma_par=suma_par+yData[i]
			else:
				suma_impar=suma_impar+yData[i]				
		return (h/3)*(yData[0]+yData[n]+4*suma_impar+2*suma_par)

def simpson38(f, x0, xn, n):
	xData=np.linspace(x0, xn, num=n+1)
	h=(xn-x0)/n
	yData=np.round(f(xData),5)
	if n%3!=0:
		print('no se puede aplicar este metodo pues n no es multiplo de 3')
		return 
	else:
		imprimir_datos(xData, yData)
		suma_mult3=0
		suma_restantes=0
		for i in range(1,n):
			if i%3==0:
				suma_mult3=suma_mult3+yData[i]
			else:
				suma_restantes=suma_restantes+yData[i]
		return (3*h/8)*(yData[0]+yData[n]+2*suma_mult3+3*suma_restantes)


def imprimir_datos(xData, yData): 		
		print('{}		{}		{}'.format('i', 'xi', 'yi'))
		for i in range(len(xData)):
			print('{}		{}		{}'.format(i, xData[i], yData[i]))


#---------------------------------------
def f(x): return (1/np.sqrt(np.pi*2))*np.exp(-0.5*x**2)


#trapecial=trapecial(f,0,1.2,2)
simpson13=simpson13(f,-3,-0.6,2)
simpson38=simpson38(f,-0.6,3,3)

#print(trapecial)
print(simpson13)
print(simpson38)
print((simpson13+simpson38))
