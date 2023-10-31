import csv
from datetime import datetime, timedelta

# Nombre de los archivos
archivo_entrada = "data.csv"
archivo_salida = "projects.csv"

# Lectura archivo de entrada
with open(archivo_entrada, newline="") as archivo:
    lectura = csv.reader(archivo)
    datos = list(lectura)

# Creación diccionario de responsables
responsables = {}
responsable_id = 1

# Crea un archivo de salida
with open(archivo_salida, mode="w", newline="") as nuevo:
    escritor = csv.writer(nuevo)

    # Escritura de la primera línea del archivo de salida
    escritor.writerow(["name", "start_date", "end_date", "assigned"])

    # Procesamiento de los proyectos
    for proyecto in datos[1:]:
        nombre_proyecto = proyecto[0]
        fecha_finalizacion = datetime.strptime(proyecto[1], "%d-%m-%Y")
        fecha_inicio = fecha_finalizacion - timedelta(days=7)
        responsable = proyecto[2]

        # Si el responsable no está en el diccionario, lo agrego
        if responsable not in responsables:
            responsables[responsable] = responsable_id
            responsable_id += 1

        # Escritura de la fila en el archivo de salida
        escritor.writerow([nombre_proyecto, fecha_inicio.strftime("%d-%m-%Y"), proyecto[1], responsables[responsable]])

    # Linea en blanco (Separación)
    escritor.writerow([])

    # Escritura ids
    escritor.writerow(["Id", "Name"])
    for id, name in responsables.items():
        escritor.writerow([name , id])



