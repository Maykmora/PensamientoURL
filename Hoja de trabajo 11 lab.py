#Primer Ejercicio 

# class ExperimentoFisico:
#     def realizar_experimento(self):
#         raise NotImplementedError("Este método debe ser implementado por las subclases")

# class CaidaLibre(ExperimentoFisico):
#     def __init__(self, altura, gravedad=9.8):
#         if altura < 0:
#             raise ValueError("La altura no puede ser negativa")
#         if gravedad <= 0:
#             raise ValueError("La gravedad debe ser mayor que cero")
        
#         self.altura = altura
#         self.gravedad = gravedad
    
#     def calcular_tiempo_caida(self):
#         """Calcula el tiempo de caída libre usando la fórmula t = √(2h/g)"""
#         return (2 * self.altura / self.gravedad) ** 0.5  
    
#     def realizar_experimento(self):
#         """Implementación del método abstracto"""
#         try:
#             tiempo = self.calcular_tiempo_caida()
#             return f"El tiempo de caída desde {self.altura}m con gravedad {self.gravedad}m/s² es: {tiempo:.2f}s"
#         except ValueError as e:
#             return f"Error en el experimento: {str(e)}"

# if __name__ == "__main__":
#     try:
#         experimento1 = CaidaLibre(altura=199, gravedad=9.8)
#         print(experimento1.realizar_experimento())
        
#     except ValueError as e:
#         print(f"Error al crear el experimento: {e}")

#segundo ejercicio
# class OperacionCientifica:
#     def calcular(self):
#         return "Método calcular() debe ser implementado en las subclases"

# class RaizCuadrada(OperacionCientifica):
#     def __init__(self, numero):
#         self.numero = numero
    
#     def calcular(self):
#         if self.numero < 0:
#             return "Error: No se puede calcular la raíz cuadrada de un número negativo"
#         if self.numero == 0:
#             return 0
        
#         aproximacion = self.numero / 2.0
#         for _ in range(20):  
#             aproximacion = 0.5 * (aproximacion + self.numero / aproximacion)
        
#         return aproximacion

# class Potencia(OperacionCientifica):
#     def __init__(self, base, exponente):
#         self.base = base
#         self.exponente = exponente
    
#     def calcular(self):
#         resultado = 1
#         for _ in range(int(self.exponente)):
#             resultado *= self.base
#         return resultado

# class Logaritmo(OperacionCientifica):
#     def __init__(self, numero, base=10):
#         self.numero = numero
#         self.base = base
    
#     def calcular(self):
#         if self.numero <= 0:
#             return "Error: No se puede calcular el logaritmo de un número no positivo"
#         if self.base <= 0 or self.base == 1:
#             return "Error: La base del logaritmo debe ser positiva y diferente de 1"
#         resultado = 0
#         valor = self.numero
#         while valor >= self.base:
#             valor /= self.base
#             resultado += 1
#         return resultado

# class Factorial(OperacionCientifica):
#     def __init__(self, numero):
#         self.numero = numero
    
#     def calcular(self):
#         if not isinstance(self.numero, int):
#             return "Error: El factorial solo está definido para números enteros"
#         if self.numero < 0:
#             return "Error: No se puede calcular el factorial de un número negativo"
        
#         resultado = 1
#         for i in range(1, self.numero + 1):
#             resultado *= i
#         return resultado

# if __name__ == "__main__":
#     operaciones = [
#         RaizCuadrada(25),
#         RaizCuadrada(-9),
#         Potencia(2, 3),
#         Logaritmo(100),
#         Logaritmo(-5),
#         Factorial(5),
#         Factorial(2.5),
#         Factorial(-3)
#     ]
    
#     for op in operaciones:
#         print(f"{op.__class__.__name__}: {op.calcular()}")