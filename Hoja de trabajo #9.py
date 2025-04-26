# #Ejercicio #1
# def es_par_o_impar(n):
#     if n % 2 == 0:
#         print(f"{n} es par")
#     else:
#         print(f"{n} es impar")
# es_par_o_impar(4)
# es_par_o_impar(5)

#Ejercicio #2
# def suma_lista(lista):
#     suma = 0
#     for numero in lista:
#         suma += numero
#     return suma
# numeros = [1, 2, 3]
# resultado = suma_lista(numeros)
# print("La suma de la lista",numeros, "es" ,resultado,)

#Ejercicio #3
# def cuenta_regresiva(n):
#     if n<0:     
#         print("¡¡DDEESSPPEEGGUUEE!!")
#     else:
#         print(n)
#         cuenta_regresiva(n-1)
# cuenta_regresiva(5)

#Ejercicio #4 
# def cuenta_ascendente(n):
#     if n < 1:
#         print("El número debe ser mayor que 0")
#     else:
#         if n == 1:
#             print(1)
#         else:
#             cuenta_ascendente(n-1)
#             print(n)

# cuenta_ascendente(5)

#Ejercicio #5 

# def suma_hasta(n):
#     if n < 0:
#         print("El número debe ser mayor que 0")
#     else:
#         suma = n * (n + 1) // 2
#         print("La suma es:", suma)

# suma_hasta(5)

#Ejercicio #6 
# def factorial(n):
#     resultado = 1
#     for i in range(2, n + 1):
#         resultado *= i
#     print("El factorial es:", resultado)

# factorial(5)

#Ejercicio #7 Mínimo en lista (sin min()) Crear una función recursiva minimo(lista) que devuelva el valor más pequeño de una lista de números.
# def minimo(lista):
#     if len(lista) == 1:
#         return lista[0]
#     else:
#         min_restante = minimo(lista[1:])
#         return lista[0] if lista[0] < min_restante else min_restante
# numeros = [5, 2, 8, 1, 4]
# resultado = minimo(numeros)
# print("El mínimo de la lista", numeros, "es", resultado)

#Juego 1
# import time

# def adivina_el_numero(numero_secreto, intentos_restantes, tiempo_inicio):
#     if intentos_restantes <= 0:
#         print(f"\n¡Se acabaron los intentos! El número era {numero_secreto}.")
#         tiempo_total = time.time() - tiempo_inicio
#         print(f"Tiempo total: {tiempo_total:.2f} segundos")
#         return
    
#     try:
#         intento = int(input(f"\nIntento #{6 - intentos_restantes} (te quedan {intentos_restantes}): "))
#     except ValueError:
#         print("Por favor, ingresa un número válido.")
#         adivina_el_numero(numero_secreto, intentos_restantes, tiempo_inicio)
#         return
    
#     if intento == numero_secreto:
#         tiempo_total = time.time() - tiempo_inicio
#         print(f"\n¡Felicidades! ¡Adivinaste el número en {6 - intentos_restantes} intentos!")
#         print(f"Tiempo total: {tiempo_total:.2f} segundos")
#         return
#     elif intento < numero_secreto:
#         print("El número secreto es mayor.")
#     else:
#         print("El número secreto es menor.")
    
#     adivina_el_numero(numero_secreto, intentos_restantes - 1, tiempo_inicio)

# numero_secreto = int(time.time() * 1000) % 100 + 1 
# intentos_totales = 5

# print("Bienvenido al juego de Adivina el Número.")
# print(f"Elige un número entre 1 y 100. Tienes {intentos_totales} intentos.")
# print("¡Buena suerte!")

# tiempo_inicio = time.time()  
# adivina_el_numero(numero_secreto, intentos_totales, tiempo_inicio)
