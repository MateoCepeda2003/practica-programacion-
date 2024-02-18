import json

def buscar_camper_id(id_camper):
    try:
        with open ("campers_registrados.json","r") as file:
            data = json.load(file)
            camper = next((camper for camper in data if camper["id"] == id_camper),none)
            return camper
    except FileNotFoundError:
        print("el archivo de campers no se encuentra.")
        return None
def actualizar_camper(id_camper, nueva_informacion):
    try:
        with open("campers_registrados.json", "r") as file:
            data= json.load(file)
            camper_a_actualizar= buscar_camper_por_su_id(id_camper)
            if camper_a_actualizar:
                camper_a_actualizar.update(nueva_informacion)
                camper_indice = [i for i, camper in enumerate(data) if camper["id"]== id_camper]
                data[camper_indice[0]] = camper_a_actualizar
                with open("campers_registrados.json", "w") as file:
                    json.dum(data, file, indent=4)
                    print("camper actualizado exitosamente,")
            else:
                print("camper no se encuentra.")
    except FileExistsError:
        print("el archivo de campers no se encuentra.")

def mostrar_menu_principal():
    print("BIENVENIDOS AL PORGRAMA")
    print("SEGUIMIENTO ACADEMICO CAMPUSLANDS")
    print("1. COORDINACION ACADEMICA")
    print("2. GESTION DE TRAINERS")
    print("3. MODULOS DE REPORTES")
    opcion = input("seleccione una opcion: ")
    if opcion == "1":
        menu_coordinacion()
    
def menu_coordinacion():
    print("MENU DE COORDINACION ACADEMICA")
    print("1. registro de campers")
    print("2. ")
    opcion = input("selecicone una opcion: ")
    if opcion = "2":
        modificar_camper()
    def modificar_camper():
    id_camper = input("ingrese el id del camper a modificar: ")
    
        if opcion == "1":
    
         registrar_camper()
        
    def registrar_camper():        
        camper = {
    "id": input("ingrese el ID del camper: "),
    "nombres": input("nombres: "),
    "apellidos": input("apellidos: "),
   "direccion": input("direccion: "),
    "acudiente": input("acudiente: "),
     "telefonos": {
        "celular":  input("telefono celular. "),
        "fijo": input("telefono fijo: ")
    },
    "estado": "En proceso de Ingreso",
    "riesgo": input("nivel de riesgo: ")
    
    }    

    guardar_camper(camper)

    def guardar_camper(camper):
    
        try:
            with open ("campers_registrados.json", "r") as file:
            data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = []
    
        data.append(camper)

        with open ("campers_registrados.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Camper registrado exitosamente")
    



mostrar_menu_principal()