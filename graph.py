import matplotlib.pyplot as plt
import numpy as np
import math as mt
def expb(a,b):
    return a**(b)
def exp(x):
    return expb(np.e,x)
def log(x,b=np.e):
    if b!=None:
        return (np.log(x+0.1))/(np.log(b))
    elif b==None:
        return np.log(x+0.1)
def ln(x):
    return np.log(x+0.1)
def sin(x):
    return np.sin(x)
def cos(x):
    return np.cos(x)
def tan(x):
    return (sin(x))/(cos(x))
def sec(x):
    return 1/(cos(x))
def csc(x):
    return 1/(sin(x))
def cot(x):
    return 1/(tan(x))
def sqrt(x):
    return exp(x,1/2)
def cbrt(x):
    return exp(x,1/3)
def floor(x):
    return mt.floor(x)
def ceil(x):
    return mt.ceil(x)
def sinh(x):
    return (exp(x)-exp(-x))/2
def cosh(x):
    return (exp(x)+exp(-x))/2
def tanh(x):
    return (sinh(x)/cosh(x))
def coth(x):
    return 1/(tanh(x))
def sech(x):
    return 1/(cosh(x))
def csch(x):
    return 1/(sinh(x))
def gif(x):
    return int(x)

if __name__=="__main__":
    e=input('enter the expression : ')
    f = lambda x : eval(e)
    LX=[]
    LY=[]
    n=float(input('enter the stopping limit : '))
    i=-n
    while i<=n:
        LX.append(i)
        LY.append(f(i))
        i=i+0.01
    x=LX
    y=LY
    y1 = []
    for i in range(-int(max(y))+1,int(max(y))+1):
        y1.append(i)
    x1 = []
    for i in range(-int(max(y))+1,int(max(y))+1):
        x1.append(int(0))
    y2 = []
    for i in range(-int(n+1),int(n+1)):
        y2.append(int(0))
    x2 = []
    for i in range(-int(n+1),int(n+1)):
        x2.append(i)
    plt.plot(x1,y1,color = "black")
    plt.plot(x2,y2,color = "black")
    plt.plot(x,y,label = 'test graph',color = "blue")
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
