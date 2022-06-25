def calc(exprType):
    print ("=======================================")
    print ("Executing '" + exprType + "' expression")
    print ("=======================================")
    y = 1
    n = 3
    yi = 0
    x= 0
    xg = 0
    x1 = 0
    yg = 0
    mg = 0

    for n in range (n):
        x1= x + 0.1
        xg = 0.5*(x + x1)
        yg = y + xg*eval(str(x) + exprType + str(y))
        mg = yg + xg
        yi = y + 0.1 * mg
        y = yi
        x = x + 0.1
        print ("=======================")
        print ("Loop number " + str(n))
        print ("=======================")
        print ("xg =", xg)
        print ("yg =", yg)
        print ("mg =", mg)
        print ("yi =", yi)

 
calc("+")
calc("-")
calc("*")
calc("/")
