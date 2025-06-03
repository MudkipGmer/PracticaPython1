def ingresar_datos():
    estudiantes = {}
    print("=== Ingreso de datos ===")
    while True:
        nombre = input("Nombre del estudiante (o 'fin' para terminar): ").strip()
        if nombre.lower() == 'fin':
            break
        try:
            notas = input(f"Ingrese las calificaciones de {nombre} separadas por comas: ")
            lista_notas = [float(nota.strip()) for nota in notas.split(',')]
            estudiantes[nombre] = lista_notas
        except ValueError:
            print(" Error: asegúrate de ingresar solo números separados por comas.")
    return estudiantes

def calcular_promedios(estudiantes):
    promedios = {}
    for nombre, notas in estudiantes.items():
        if notas:
            promedio = sum(notas) / len(notas)
            promedios[nombre] = promedio
    return promedios

def obtener_mejor_estudiante(promedios):
    if not promedios:
        return None, 0
    mejor = max(promedios, key=promedios.get)
    return mejor, promedios[mejor]

def guardar_resultados(estudiantes, promedios, mejor_estudiante):
    with open("resultados.txt", "w") as f:
        f.write("=== Resultados por estudiante ===\n")
        for nombre, notas in estudiantes.items():
            promedio = promedios.get(nombre, 0)
            f.write(f"{nombre}: Notas: {notas} | Promedio: {promedio:.2f}\n")
        if mejor_estudiante[0]:
            f.write(f"\n🏅 Mejor estudiante: {mejor_estudiante[0]} con promedio {mejor_estudiante[1]:.2f}\n")
        else:
            f.write("\nNo hay estudiantes para evaluar.\n")

def main():
    estudiantes = ingresar_datos()
    promedios = calcular_promedios(estudiantes)
    mejor_estudiante = obtener_mejor_estudiante(promedios)
    guardar_resultados(estudiantes, promedios, mejor_estudiante)
    print(" Resultados guardados en 'resultados.txt'")

if __name__ == "__main__":
    main()
