# Importamos las librerías necesarias
import json

# Definimos las clases
class Camper:
    def __init__(self, id, nombres, apellidos, direccion, acudiente, telefonos, estado, riesgo):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.acudiente = acudiente
        self.telefonos = telefonos
        self.estado = estado
        self.riesgo = riesgo

class Ruta:
    def __init__(self, nombre, modulos, sgdb_principal, sgdb_alternativo):
        self.nombre = nombre
        self.modulos = modulos
        self.sgdb_principal = sgdb_principal
        self.sgdb_alternativo = sgdb_alternativo

class Trainer:
    def __init__(self, id, nombres, apellidos, telefono, rutas):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.rutas = rutas

# Funciones para CRUD

def crear_camper(camper):
    with open("campers.json", "r+") as archivo:
        campers = json.load(archivo)
        campers.append(camper.__dict__)
        archivo.seek(0)
        json.dump(campers, archivo, indent=4)

def obtener_campers():
    with open("campers.json", "r") as archivo:
        campers = json.load(archivo)
        return campers

def actualizar_camper(camper):
    with open("campers.json", "r+") as archivo:
        campers = json.load(archivo)
        for i, c in enumerate(campers):
            if c["id"] == camper.id:
                campers[i] = camper.__dict__
                archivo.seek(0)
                json.dump(campers, archivo, indent=4)
                break

def eliminar_camper(id):
    with open("campers.json", "r+") as archivo:
        campers = json.load(archivo)
        campers = [c for c in campers if c["id"] != id]
        archivo.seek(0)
        json.dump(campers, archivo, indent=4)

# Funciones adicionales

def calcular_promedio(nota_teorica, nota_practica):
    return (nota_teorica * 0.3) + (nota_practica * 0.6)

def evaluar_modulo(nota_final):
    return "Aprobado" if nota_final >= 60 else "Reprobado"

# Programa principal

# Inicializamos la lista de campers
campers = []

# Opciones del menú


while True:
    print("-" * 50)
    print("**Seguimiento académico CampusLands**")
    print("-" * 50)
    print("1. Registrar camper")
    print("2. Mostrar campers")
    print("3. Evaluar camper")
    print("4. Salir")
    print("-" * 50)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Registrar un nuevo camper
        id = int(input("Ingrese el ID del camper: "))
        nombres = input("Ingrese los nombres del camper: ")
        apellidos = input("Ingrese los apellidos del camper: ")
        direccion = input("Ingrese la dirección del camper: ")
        acudiente = input("Ingrese el nombre del acudiente: ")
        telefonos = input("Ingrese los teléfonos del camper (separados por coma): ")
        estado = "En proceso de ingreso"
        riesgo = "Bajo"

        # Creamos un nuevo objeto Camper
        camper = Camper(id, nombres, apellidos, direccion, acudiente, telefonos.split(","), estado, riesgo)

        # Guardamos el camper en el archivo JSON
        crear_camper(camper)

    elif opcion == "2":
        # Mostrar la lista de campers
        campers = obtener_campers()
        for camper in campers:
            print(f"ID: {camper['id']}")
            print(f"Nombres: {camper['nombres']}")
            print(f"Apellidos: {camper['apellidos']}")
            print(f"Estado: {camper['estado']}")
            print("-" * 20)

    elif opcion == "3":
    # Evaluar un camper
        id = int(input("Ingrese el ID del camper a evaluar: "))

    # Buscamos el camper en la lista
    camper = next((c for c in campers if c["id"] == id), None)

    if camper is None:
        print("Camper no encontrado.")
        continue

    # Obtenemos las notas del camper
    nota_teorica = float(input("Ingrese la nota teórica del módulo: "))
    nota_practica = float(input("Ingrese la nota práctica del módulo: "))

    # Calculamos el promedio
    promedio = calcular_promedio(nota_teorica, nota_practica)

    # Evaluamos el módulo
    evaluacion = evaluar_modulo(promedio)

    # Actualizamos el estado del camper
    if evaluacion == "Aprobado":
        camper["estado"] = "Aprobado"
    else:
        camper["estado"] = "Reprobado"

    # Actualizamos el camper en el archivo JSON
    actualizar_camper(camper)

    print(f"Evaluación del módulo: {evaluacion}")

         
    # Salir del programa
    print("¡Hasta pronto!")
    break

else:
    print("Opción no válida.")
