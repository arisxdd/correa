#ejecutar menu
import random

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez",
                 "Ana Martinez", "Pedro Rodrigez", "Laura Hernandez", "Miguel Sanchez",
                 "Isabel Gomez", "Francisco Diaz", "Helena Fernandez"]

sueldos ={}
def asignar_sueldo_aleatorios():
    for trabajador in trabajadores:
        sueldos[trabajador] = random.randint(300.000, 2.500000)
        print("sueldos asignados aleatoriamente\n")

def clasificar_sueldos():
    if not sueldos:
        print("Primero debes asignar un sueldo\n") 
        return    
print("Clasificacion de sueldos:")
for trabajador, sueldo in sueldos.items():
    if sueldo < 1000000:
        clasificacion = "bajo"
    elif 1000000 <= sueldo <2000000:
        clasificacion = "medio"
    else:
        clasificacion = "alto"
        print(f"{trabajador}: ${sueldo}-{clasificacion}")

def ver_estadistica():
    if not sueldos:
        print("Primero debes asignar un sueldos.\n")
        return
    
sueldos_list = list(sueldos.values())
max_sueldo = max(sueldos_list)
min_sueldo = min(sueldos_list)
promedio = sum(sueldos_list)/len(sueldos_list)
print(f"Sueldo maximo: ${max_sueldo}")
print(f"Sueldo minimo: ${min_sueldo}")
print(f"sueldo promedio: ${promedio:.2f}\n")

def reporte_de_sueldo():
    print("Reporte de sueldos:")
for trabajador, sueldo in sueldos.items():
    print(f"{trabajador}: ${sueldo}")   

def menu():    
   while True:
        print("\nMenu de opciones:")
        print("1.Asignar sueldo aleatorio")
        print("2.Clasificar sueldos")
        print("3.Ver estadistica")
        print("4.Reporte de sueldo")
        print("5.Salir del programa")       

opcion =input("Seleccione una opcion:")

if opcion =="1":
    asignar_sueldo_aleatorios()
elif opcion =="2":
    clasificar_sueldos()
elif opcion =="3":
    ver_estadistica()
elif opcion =="4":
    reporte_de_sueldo()
elif opcion =="5":
      print("saliendo del programa...") 
else:
    print("Opcion no valida")

menu()








