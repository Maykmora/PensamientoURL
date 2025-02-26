print("Bienvenido al programa")

v1=int(input("Ingrese un numero de 5 digitos:"))
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
n7=0
n8=0

if v1>10000 and v1<=99999:                                   #v1=12345
    print("El numero de 5 digitos es valido")
    n1=v1%10000                                             #n1=2345
    n2=n1%1000                                              #n2=345
    n3=n2%100                                               #n3=45
    e=n3%10                                                #e=5   quinto digito  n4
    a=v1//10000                                            #a=1  primer digito   n5
    b=n1//1000                                             #b=2   segundo digito n6
    c=n2//100                                              #c=3   tercer digito  n7
    d=n3//10                                               #d=4   cuarto digito  n8
    
    if a>b:
        a,b=b, a 
    if a>c:
        a, c=c, a 
    if a>d:
        a, d=d, a 
    if a>e:
        a, e= e, a
    if b>c:
        b, c=c, d 
    if b>d:
        b, d=d,b 
    if b>e:
        b, e=e, b 
    if c>d:
        c, d=d, c 
    if c>e:
        c, e=e, c 
    if d>e:
        d, e=e, d 
    
    print("Los digitos ordenados en orden ascendente son:", a, b, c, d, e)
    
    
    if a<b:
        b,a=a, b 
    if a<c:
        c, a=a, c 
    if a<d:
        d, a=a, d 
    if a<e:
        e, a= a, e
    if b<c:
        c, b=b, c 
    if b<d:
        d, b=b,d 
    if b<e:
        e, b=b, e 
    if c<d:
        d, c=c, d 
    if c<e:
        e, c=c, e 
    if d<e:
        e, d=d, e 
    
    print("Los digitos ordenados en orden descendente son:", a, b, c, d, e)
    
else:
    print("Error Intentelo De Nuevo")
   
    