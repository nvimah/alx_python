def comb(L):  
    a=int(input("Enter first number:"))  
    b=int(input("Enter second number:"))  
    c=int(input("Enter third number:"))  
    d=int(input("Enter fourth number:"))  
    e=int(input("Enter fifth number:"))  
    f=int(input("Enter sixth number:"))  
    g=int(input("Enter seventh number:"))  
    h=int(input("Enter eigth number:"))  
    i=int(input("Enter ninth number:"))  
    j=int(input("Enter tenth number:"))   


    L.append(a)  
    L.append(b)  
    L.append(c)  
    L.append(d)  
    L.append(e)  
    L.append(f)  
    L.append(g)  
    L.append(h)  
    L.append(i)  
    L.append(j)  
    
    for m in range(10):  
        for n in range(10):  
            #for n in range(10):  
                  
                # check if the indexes are not  
                # same  
                if (m!=n and n!=m ):  
                    print(L[m], L[n])  
                      
comb([])  