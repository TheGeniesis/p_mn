import numpy as np
import matplotlib.pyplot as plt
 
def printGrid(x, y): 
    plt.plot(x, y, '-r', label='y=2x+1')
    plt.title('Func y=ax+b')
    plt.xlabel('x', color='black')
    plt.ylabel('y', color='black')
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()    

def formula11():
    n = [1,2,3,4,5,6,7,8,9,10]
    l = [10,18,22,27,36,49,56,64,70,78]

    sumN = sum(n)
    sumL = sum(l)

    sumN2 = sum(i*i for i in n)
    nl = ([x*y for x,y in zip(n,l)])
    sumNL = sum(nl)

    print("Sum N:", sumN)
    print("Sum L:", sumL)
    print("Sum N2:", sumN2)
    print("Sum LN", SumNL)

    a = np.array([ [10,sumN], [sumN,sumN2] ])
    b = np.array([sumL,SumNL])
    z = np.linalg.solve(a,b)
    print(z)

    x = np.linspace(0,10,100)
    y = z[1]*x+z[0]

    printGrid(x,y)

formula11()
