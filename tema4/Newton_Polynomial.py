## Newton Divided Difference Polynomial Interpolation Method

import numpy as np
x = np.array([1.0,1.5,2.0])
y = np.array([ 1.81636,0.58773,-0.56162])
'''
x=np.array([0,1,2,5.5,11,13,16,18],float)
y=np.array([0.5,  3.134,  5.9,  9.9,  10.2,  9.35,  7.2,  6.2],float)
'''
n=len(x)
p=np.zeros([n,n+1])#creating a Tree table (n x n+1 array)
value =float(input("Enter the point at which you want to calculate the value of the polynomial: "))
# first two columns of the table are filled with x and y data points
for i in range(n):

        p[i,0]=x[i]
        p[i,1]=y[i]

## algorithm for tree table from column 2 two n+1        
for i in range(2,n+1): #column
  for j in range(n+1-i):# defines row
    p[j,i]=(p[j+1,i-1]-p[j,i-1])/(x[j+i-1]-x[j])#Tree Table
np.set_printoptions(suppress=True)## this suppress the scientific symbol(e) and returns values in normal digits

# print(p) ## can check the complete Tree table here for NDDP
b=p[0][1:]#This vector contains the unknown coefficients in the polynomial which are the top elements of each column. 
print("b= ",b)
print("x= ",x)
lst=[] # list where we will append the values of prouct terms

t=1
for i in range(len(x)):
    t*=(value-x[i]) ##(x-x0), (x-x0)(x-x1), (x-x0)(x-x1)(x-x2) etc..
    lst.append(t)
print("The list of product elements ",lst,end = ' ')
## creating a general function
f=b[0]
for k in range(1,len(b)):
  f+=b[k]*lst[k-1] ## important**[k-1]** not k because in list we use one step earlier element. For example for b1 we have to use (x-x0), for b2, we use (x-x0)(x-x1) for b3 we use (x-x0)(x-x1)(x2)
print("The value of polynomial: ","%.3f"%f)