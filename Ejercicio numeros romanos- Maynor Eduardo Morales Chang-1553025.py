print("PROGRAMA DE EQUIVALENCIA DE NUMEROS ROMANOS")

V=int(input("Ingrese un valor del 1 al 9:"))
R=''

if V<1:
    print("valor invalido, intentelo de nuevo")
elif V<=3:
    resul=V*'I'
    print("El numero",V, "en numeros romanos es:", resul,)
elif V==4:
    print("El numero 4 en numeros romanos es: IV")
elif V>=5 and V<=8:
    resul='V'+(V-5)*'I'
    print("El numero",V, "en numeros romanos es:", resul,)
elif V==9:
    print("El numero 9 en numeros romanos es: IX")
    
else:
    print("Valor invalido, intentelo de nuevo")

