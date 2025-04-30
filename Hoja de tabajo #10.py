# Primer ejercicio de la hoja de trabajo #10
# class Animal:
#     def __init__(self, nombre, edad, peso):
#         self.nombre = nombre
#         self.edad = edad
#         self.peso = peso

#     def mostrar_datos_medicos(self):
#         return f"Nombre: {self.nombre}\nEdad: {self.edad} años\nPeso: {self.peso} kg"

#     def calcular_dosis_medicamento(self):
#         pass

#     def generar_ficha_medica(self):
#         return f"Ficha médica de {self.nombre}:\n{self.mostrar_datos_medicos()}\n"

# class Perro(Animal):
#     def __init__(self, nombre, edad, peso, raza):
#         super().__init__(nombre, edad, peso)
#         self.raza = raza

#     def calcular_dosis_medicamento(self):
#         dosis = self.peso * 0.05  
#         return f"Dosis recomendada para {self.nombre}: {dosis} ml de medicamento."

#     def generar_ficha_medica(self):
#         return super().generar_ficha_medica() + f"Raza: {self.raza}\n"


# class Gato(Animal):
#     def __init__(self, nombre, edad, peso, color):
#         super().__init__(nombre, edad, peso)
#         self.color = color

#     def calcular_dosis_medicamento(self):
#         dosis = self.peso * 0.04  
#         return f"Dosis recomendada para {self.nombre}: {dosis} ml de medicamento."

#     def generar_ficha_medica(self):
#         return super().generar_ficha_medica() + f"Color: {self.color}\n"


# class Ave(Animal):
#     def __init__(self, nombre, edad, peso, tipo):
#         super().__init__(nombre, edad, peso)
#         self.tipo = tipo

#     def calcular_dosis_medicamento(self):
#         dosis = self.peso * 0.02  
#         return f"Dosis recomendada para {self.nombre}: {dosis} ml de medicamento."

#     def generar_ficha_medica(self):
#         return super().generar_ficha_medica() + f"Tipo: {self.tipo}\n"


# class Reptil(Animal):
#     def __init__(self, nombre, edad, peso, habitat):
#         super().__init__(nombre, edad, peso)
#         self.habitat = habitat

#     def calcular_dosis_medicamento(self):
#         dosis = self.peso * 0.03 
#         return f"Dosis recomendada para {self.nombre}: {dosis} ml de medicamento."

#     def generar_ficha_medica(self):
#         return super().generar_ficha_medica() + f"Hábitat: {self.habitat}\n"


# peluso = Perro("Peluso", 11, 8, "Poodle")
# mizo= Gato("Mizo", 3, 5, "Anaranjado")
# liro= Ave("Liro", 6, 0.5, "Tropical")
# igor= Reptil("Igor", 4, 1.2, "Selva")
# print("\n")
# print(peluso.mostrar_datos_medicos())
# print(peluso.calcular_dosis_medicamento())
# print("\n")
# print(peluso.generar_ficha_medica())

# print("\n")

# print(mizo.mostrar_datos_medicos())
# print(mizo.calcular_dosis_medicamento())
# print("\n")
# print(mizo.generar_ficha_medica())

# print("\n")

# print(liro.mostrar_datos_medicos())
# print(liro.calcular_dosis_medicamento())
# print("\n")
# print(liro.generar_ficha_medica())

# print("\n")

# print(igor.mostrar_datos_medicos())
# print(igor.calcular_dosis_medicamento())
# print("\n")
# print(igor.generar_ficha_medica())


#Segundo ejercicio de la hoja de trabajo #10

# class Persona:
#     def __init__(self, nombre, edad, dni):
#         self.nombre = nombre
#         self.edad = edad
#         self.dni = dni

#     def mostrar_informacion(self):
#         return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

# class Estudiante(Persona):
#     def __init__(self, nombre, edad, dni, carrera, año_estudio):
#         super().__init__(nombre, edad, dni)
#         self.carrera = carrera
#         self.año_estudio = año_estudio

#     def mostrar_informacion(self):
#         info_base = super().mostrar_informacion()
#         return f"{info_base}, Carrera: {self.carrera}, Año de Estudio: {self.año_estudio}"

# class Profesor(Persona):
#     def __init__(self, nombre, edad, dni, materia, años_experiencia):
#         super().__init__(nombre, edad, dni)
#         self.materia = materia
#         self.años_experiencia = años_experiencia

#     def mostrar_informacion(self):
#         info_base = super().mostrar_informacion()
#         return f"{info_base}, Materia: {self.materia}, Años de Experiencia: {self.años_experiencia}"

# class Administrativo(Persona):
#     def __init__(self, nombre, edad, dni, puesto, departamento):
#         super().__init__(nombre, edad, dni)
#         self.puesto = puesto
#         self.departamento = departamento

#     def mostrar_informacion(self):
#         info_base = super().mostrar_informacion()
#         return f"{info_base}, Puesto: {self.puesto}, Departamento: {self.departamento}"

# juanito= Estudiante("Juan Pérez", 20, "12345678", "Ingeniería", 2)
# maria= Profesor("María López", 45, "87654321", "Matemáticas", 20)
# carlos= Administrativo("Carlos García", 38, "11223344", "Secretario", "Recursos Humanos")

# print("\n")
# print(juanito.mostrar_informacion())
# print("\n")
# print(maria.mostrar_informacion())
# print("\n")
# print(carlos.mostrar_informacion())
# print("\n")
