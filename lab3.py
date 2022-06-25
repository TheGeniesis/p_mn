def calc(exprType):
    print ("=======================================")
    print ("Executing '" + exprType + "' expression")
    print ("=======================================")
    y = 1
    n = 3
    yi = 0
    x= 0
    # x*
    xg = 0
    #xi+1
    x1 = 0
    # y*
    yg = 0
    # m*
    mg = 0
    h=0.1

    for n in range (n):
        x1 = x + h
        # x* = 0.5(xi+xi+1)
        xg = 0.5*h*(x + x1)
        # y*=yi+0.5hF(xi,yi)
        yg = y + 0.5*h*eval(str(x) + exprType + str(y))
        # m* = F(x*,y*)
        mg = xg + yg
        yi = y + h * mg
        y = yi
        x = x + h
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
