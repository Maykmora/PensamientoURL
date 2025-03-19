saldoin=3000
intentosFallidos=0 

#transacción 
while True: 
    print(f"Su saldo actual es: Q{saldoin}")
    monto=int(input("Ingrese la cantidad a retirar:"))

    if monto==0:
        print("Gracias por utilizar el cajero, adios.")
        break
    try:
        monto=int(monto)
    except ValueError:
        print("Por favor ingrese un monto válido")
        continue
    if monto>saldoin:
        intentosFallidos+=1
        if intentosFallidos>=3:
            print("Demasiados intentos fallidos, adios.")
            break 
        print(f"Saldo insuficiente, intentos restantes:{3-intentosFallidos}")
    else: 
        saldoin-=monto
        if saldoin==0:
            print("Retiro exitoso, su saldo esta agotado. ")
            break
        else: 
            print(f"Retiro exitoso, su saldo actual es: Q{saldoin}")
print("Gracias por utilizar el cajero, adios.") 
