from matplotlib import pyplot as plt
import numpy

x=[-2,0,2]
y=[4,0,4]


def formula3(x,y, elem):
    loopIndex=0
    xi=1
    result=0

    while(loopIndex < len(x)-1):
        result+=y[loopIndex]*((elem-x[loopIndex])*(elem-x[loopIndex+1])/ \
               (xi-x[loopIndex])*(xi-x[loopIndex+1]))
        loopIndex+=1
        xi+=1

    return result

def formula4(x, y):
    return (y[0]/((x[0]-x[1])*(x[0]-x[2])))+ \
           (y[1]/((x[1]-x[0])*(x[1]-x[2])))+ \
           (y[2]/((x[2]-x[0])*(x[2]-x[1])))

def formula5(x, y):
    return (-y[0]*(x[1]+x[2])/((x[0]-x[1])*(x[0]-x[2])))- \
            (y[1]*(x[0]+x[2])/((x[1]-x[0])*(x[1]-x[2])))- \
            (y[2]*(x[0]+x[1])/((x[2]-x[0])*(x[2]-x[1])))

def formula6(x,y):
    return (y[0]*x[1]*x[2]/((x[0]-x[1])*(x[0]-x[2])))+ \
           (y[1]*x[0]*x[2]/((x[1]-x[0])*(x[1]-x[2])))+ \
           (y[2]*x[0]*x[2]/((x[2]-x[0])*(x[2]-x[1])))


a=formula4(x,y)
b=formula5(x,y)
c=formula6(x,y)

print(a)
print(b)
print(c)

# graph info
x=numpy.linspace(-2,2,100)

# func
z=a*x**2+b*x+c

pyplot.plot(x, z)
pyplot.show()

x=[-10,-8,-6,-4,-2,2,4,6,8,10]
y=[20,16,12,8,4,4,8,12,16,20]
print(formula3(x,y,4))
