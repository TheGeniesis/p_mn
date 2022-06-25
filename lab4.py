# F(x; y) = a  x <expr> b  y:
def calcRK3(exprType):
    # Basic idea from slides:
    # m1 = x+y
    # m2=x + 1/2*h+y+1/2*h*m1
    # m3=x+h+y-h*m1+2*h*m2

    # x=x+h
    # y=y+((h/6)(m1+4*m2+m3))
    
    print ("=======================================")
    print ("Executing '" + exprType + "' expression")
    print ("=======================================")
    
    # consts
    h=0.1
    n=2
    a=1
    b=2
    
    # calculations
    x=0
    y=1
    for n in range (n):
        print ("=======================")
        print ("Step number " + str(n))
        print ("=======================")        
        # let's simplify and set parts of query to variables
        # if sth change with main expression, then we will need to change only x and y here
        # x and y are equal to elems from slides
        # if we comment these lines then we will receive the same result like we got in slides
        x = a*x 
        y = b*y
    
        # x<expr>y
        m1expr=str(x)+exprType+str(y)
        print("m1 =", m1expr)
        m1=eval(m1expr)
        print ("m1 =", m1)

        # x+(1/2)h<expr>y+(1/2)h*m1)
        m2expr=str(x)+"+(1/2)*"+str(h)+exprType+str(y)+"+(1/2)*"+str(h)+"*"+str(m1)
        print("m2 =", m2expr)
        m2=eval(m2expr)
        print ("m2 =", m2)

        # x+h<expr>y-hm1+2hm2
        m3expr=str(x)+"+"+str(h)+exprType+str(y)+"-"+str(h)+"*"+str(m1)+"+2*"+str(h)+"*"+str(m2)
        print("m3 =", m3expr)
        m3=eval(m3expr)
        print ("m3 =", m3)

        x=x+h
        print("x =", x)     
        y=y+((h/6)*(m1+4*m2+m3))
        print ("y =", y)
    

 
calcRK3("+")
calcRK3("-")
calcRK3("*")
calcRK3("/")


# F(x; y) = a  x <expr> b  y:
def calcRK4(exprType):
    print ("=======================================")
    print ("Executing '" + exprType + "' expression")
    print ("=======================================")
    
    # consts
    h=0.1
    n=3
    a=1
    b=2
    
    # calculations
    x=0
    y=1
    for n in range (n):
        print ("=======================")
        print ("Step number " + str(n))
        print ("=======================")        
        # let's simplify and set parts of query to variables
        # if sth change with main expression, then we will need to change only x and y here
        # x and y are equal to elems from slides
        # if we comment these lines then we will receive the same result like we got in slides
        x = a*x 
        y = b*y
    
        # x<expr>y
        m1expr=str(x)+exprType+str(y)
        print("m1 =", m1expr)
        m1=eval(m1expr)
        print ("m1 =", m1)

        # x+(1/2)h<expr>y+(1/2)h*m1)
        m2expr=str(x)+"+(1/2)*"+str(h)+exprType+str(y)+"+(1/2)*"+str(h)+"*"+str(m1)
        print("m2 =", m2expr)
        m2=eval(m2expr)
        print ("m2 =", m2)

        # x+1/2h<expr>y+(1/2)*hm2
        m3expr=str(x)+"+(1/2)*"+str(h)+exprType+str(y)+"+(1/2)*"+str(h)+"*"+str(m1)+"*"+str(m2)
        print("m3 =", m3expr)
        m3=eval(m3expr)
        print ("m3 =", m3)


        # x+h<expr>y+hm3
        m4expr=str(x)+"+"+str(h)+exprType+str(y)+"+"+str(h)+"*"+str(m3)
        print("m4 =", m4expr)
        m4=eval(m4expr)
        print ("m4 =", m4)        
        
        x=x+h
        print("x =", x)     
        y=y+((h/6)*(m1+2*m2+2*m3+m4))
        print ("y =", y)
    

 
calcRK4("+")
calcRK4("-")
calcRK4("*")
calcRK4("/")
