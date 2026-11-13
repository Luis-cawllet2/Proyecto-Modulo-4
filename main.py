
# Proyecto Módulo 4 - Tabla de posiciones
 
# Clase que agrupa los datos de un equipo
class Equipo:
    def __init__(self, nombre, ganados, perdidos, empates, puntos):
        self.nombre = nombre
        self.ganados = ganados
        self.perdidos = perdidos
        self.empates = empates
        self.puntos = puntos
 
print(" TABLA DE POSICIONES ")
 
# Pedir y validar los datos generales
num_equipos = int(input("¿Cuántos equipos hay? "))
while num_equipos < 2:
    num_equipos = int(input("Debe haber al menos 2 equipos: "))
 
num_partidos = int(input("¿Cuántos partidos jugó cada equipo? "))
while num_partidos < 1:
    num_partidos = int(input("Debe ser al menos 1 partido: "))
 

equipos = []
matriz = []
 
# Capturar los resultados de cada equipo
for i in range(num_equipos):
    nombre = input(f"\nNombre del equipo {i + 1}: ")
    fila = []
    ganados = 0
    perdidos = 0
    empates = 0
 
    for j in range(num_partidos):
        resultado = input(f"Partido {j + 1} de {nombre} (G=ganado, P=perdido, E=empate): ").upper()
        
        while resultado != "G" and resultado != "P" and resultado != "E":
            resultado = input("Opción no válida. Escribe G, P o E: ").upper()
 
        if resultado == "G":
            fila.append(3)
            ganados += 1
        elif resultado == "P":
            fila.append(0)
            perdidos += 1
        else:
            fila.append(1)
            empates += 1
 
   
    puntos = 0
    for p in fila:
        puntos += p
 
    matriz.append(fila)
    equipos.append(Equipo(nombre, ganados, perdidos, empates, puntos))
 
# Mostrar la matriz de puntos
print("\n Matriz de puntos ")
for i in range(num_equipos):
    print(f"{equipos[i].nombre}: {matriz[i]}")
 
# Mostrar la tabla de resultados
print("\n Resultados ")
for eq in equipos:
    print(f"{eq.nombre} | G: {eq.ganados} | P: {eq.perdidos} | E: {eq.empates} | Puntos: {eq.puntos}")
 
# Buscar al líder (el equipo con más puntos)
lider = equipos[0]
for eq in equipos:
    if eq.puntos > lider.puntos:
        lider = eq
 
print(f"\nEl líder es {lider.nombre} con {lider.puntos} puntos.")