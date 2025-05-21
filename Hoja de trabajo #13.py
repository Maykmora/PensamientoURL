matriz = [
 [0,0,0,0,0,0,0,1,1,0],
 [0,1,1,0,0,0,0,0,0,0],
 [0,1,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,1,0],
]


def imprimir_tablero(matriz):
    for fila in matriz:
        print(fila)
    print()

def contar_vecinos(fila, columna, matriz):
    vecinos = 0
    filas = len(matriz)
    columnas = len(matriz[0])
    if columna - 1 >= 0:
        vecinos += matriz[fila][columna - 1]
    if columna + 1 < columnas:
        vecinos += matriz[fila][columna + 1]
    if fila - 1 >= 0 and columna - 1 >= 0:
        vecinos += matriz[fila - 1][columna - 1]
    if fila - 1 >= 0 and columna + 1 < columnas:
        vecinos += matriz[fila - 1][columna + 1]
    if fila + 1 < filas and columna - 1 >= 0:
        vecinos += matriz[fila + 1][columna - 1]
    if fila + 1 < filas and columna + 1 < columnas:
        vecinos += matriz[fila + 1][columna + 1]
    return vecinos

def siguiente_generacion(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    nueva_matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            vecinos = contar_vecinos(i, j, matriz)
            celula = matriz[i][j]
            
            if celula == 1:
                if vecinos in [1, 2]:
                    nueva_matriz[i][j] = 1
                else:
                    nueva_matriz[i][j] = 0
            else:
                if vecinos == 1:
                    nueva_matriz[i][j] = 1
                else:
                    nueva_matriz[i][j] = 0
    return nueva_matriz

print("Generación 0:")
imprimir_tablero(matriz)
generacion_1 = siguiente_generacion(matriz)
print("Generación 1:")
imprimir_tablero(generacion_1)
generacion_2 = siguiente_generacion(generacion_1)
print("Generación 2:")
imprimir_tablero(generacion_2)
