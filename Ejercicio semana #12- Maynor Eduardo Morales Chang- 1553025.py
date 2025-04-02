#Primer Ejercicio 
# n=int(input("Ingrese el tamaño del arreglo:"))
# m=int(input("Ingrese los multiplos:"))
# arreglo=[]
# for i in range (1,n+1):
#     arreglo.append(i*m)
    
# print(arreglo)

#Segundo ejercicio
# n=int(input("Ingrese el tamaño del arreglo:"))
# arreglo1=[]
# arreglo2=[]
# while n!=0:
#     name=str(input("Ingrese el nombre:"))
#     arreglo1.append(name)
#     n=n-1

#     cant=len(name)
#     arreglo2.append(cant)

# print(arreglo1)
# print(arreglo2)    


#Escenario 1
#En el restaurante de una universidad, el cliente luego de ser atendido evalua la atencion recibida presionando un boton entre las 5 opciones: Excelente, Muy buena, Buena, Regular, Mala. Realice un algoritmo que registre en un arreglo la evaluacion para n clientes atendidos, luego debera tabular: Total de respuestas por tipo ; La respesta mas frecuente; ¿Cuales clients respondieron con valores menores al promedio 
# n=int(input("Ingrese el numero de clientes:"))
# arreglo=[]
# uno, dos, tres, cuatro, cinco = 0, 0, 0, 0, 0
# promedio=0
# div=n
# suma=0
# while n!=0:
#     nota=int(input("Ingrese la calificacion:"))
#     arreglo.append(nota)
#     promedio=promedio+nota
#     n=n-1
#     if nota==1:
#         uno=uno+1
#     elif nota==2:
#         dos=dos+1
#     elif nota==3:
#         tres=tres+1
#     elif nota==4:
#         cuatro=cuatro+1
#     elif nota==5:
#         cinco=cinco+1

# print("La lista calificaciones es:",arreglo)
# print("Malas:",uno)
# print("Regulares:",dos)
# print("Buenas:",tres)
# print("Muy Buenas:",cuatro)
# print("Excelentes:",cinco)
# p=promedio/div
# print("El promedio es:",p)
# print("Clientes con valor menor al promedio:")
# for numero in arreglo:
#     if numero<p:
#         suma+=numero
# print((suma*100)/promedio, "% ")






