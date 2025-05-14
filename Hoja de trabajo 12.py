dias=["Lunes","Martes","Miércoles","Jueves","Viernes"]

niveles_azucar = [130, 160, 95, 175, 160]   
niveles_sal = [2000, 2400, 1800, 2400, 2700] 
presion = [115, 130, 110, 125, 175]

rango_azucar = (70, 140)
limite_sal = 2300

def clasificar_presion(sistolica):
    if sistolica < 120:
        return "Normal"
    elif 120 <= sistolica <= 129:
        return "Elevada"
    elif 130 <= sistolica <= 139:
        return "Hipertensión Etapa 1"
    elif sistolica >= 140:
        return "Hipertensión Etapa 2"
    else:
        return "No clasificado"

alertas = []
for i in range(5):
    alerta_dia = {"día": dias[i], "alertas": []}
    
    if niveles_azucar[i] < rango_azucar[0]:
        alerta_dia["alertas"].append("Azúcar baja")
    elif niveles_azucar[i] > rango_azucar[1]:
        alerta_dia["alertas"].append("Azúcar alta")
    
    if niveles_sal[i] > limite_sal:
        alerta_dia["alertas"].append("Consumo de sal elevado")
    
    clasificacion = clasificar_presion(presion[i])
    if clasificacion != "Normal":
        alerta_dia["alertas"].append(f"Presión arterial: {clasificacion}")
    
    alertas.append(alerta_dia)

for alerta in alertas:
    print(f"\n{alerta['día']}:")
    if alerta["alertas"]:
        for alerta_ind in alerta["alertas"]:
            print(f"  - {alerta_ind}")
    else:
        print("  - Todo en rango saludable")


promedios = {
    "azucar": sum(niveles_azucar) / len(niveles_azucar),
    "sal": sum(niveles_sal) / len(niveles_sal),
    "presion": sum(presion) / len(presion)
}

print(f"\nPromedio semanal de azúcar: {promedios['azucar']} mg/dL")
print(f"Promedio semanal de sal: {promedios['sal']} mg")
print(f"Promedio semanal de presión arterial: {promedios['presion']} mmHg")


alerta_semanal = []
for i in range(5):
    alerta_dia = {"día": dias[i], "alertas": []}
    
    if niveles_azucar[i] < rango_azucar[0]:
        alerta_dia["alertas"].append("Azúcar baja")
    elif niveles_azucar[i] > rango_azucar[1]:
        alerta_dia["alertas"].append("Azúcar alta")
    
    if niveles_sal[i] > limite_sal:
        alerta_dia["alertas"].append("Consumo de sal elevado")

    clasificacion = clasificar_presion(presion[i])
    if clasificacion != "Normal":
        alerta_dia["alertas"].append(f"Presión arterial: {clasificacion}")
    
    alerta_semanal.append(alerta_dia)

