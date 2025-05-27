from funciones.cargar_pacientes import ingreso_pacientes as carga
from funciones.mostrar_segun import mostrar_todos as todos
from funciones.busqueda_por_historia import buscar_paciente as buscar
from funciones.ordenar_por_historia import ordenar_pacientes_ascendente as ordenar
from funciones.mostrar_segun import mostrar_paciente_mas_dias_internacion as mas_dias_internacion
from funciones.mostrar_segun import mostrar_paciente_menos_dias_internacion as menos_dias_internacion
from funciones.mostrar_segun import mostrar_mayor_5_dias_internacion as mas_5_dias_internacion
from funciones.promedio_internacion_pacientes import promedio_pacientes as promedio

opcion = 0
matriz = [[1212,"Jorge",54,"Tos",5], [1213,"carlos",44,"Fiebre",5], [1214,"Alberto",54,"Fiebre",4], [1215,"Pablo",54,"Fiebre",4]]
while(opcion != 9):
    print("MENU PRINCIPAL")
    print("1. Carga pacientes.\n" \
    "2. Mostrar todos los pacientes.\n" \
    "3. Buscar pacientes por numero de historia clinica.\n" \
    "4. Ordenar pacientes por numero de historia clinica.\n" \
    "5. Mostrar pacientes con mas dias de internacion.\n" \
    "6. Mostrar pacientes con menos dias de internacion.\n" \
    "7. Cantidad de pacientes con mas de 5 dias de internacion.\n" \
    "8. Promedio de dias de internacion de todos los pascientes.\n" \
    "9. Salir.")

    opcion = int(input("Seleccione una opcion: "))

    match opcion:
        case 1:
            cantidad = int(input("Ingrese la cantidad de pacientes que desea iongresar: "))
            carga(matriz, cantidad)
        case 2:
            todos(matriz)
        case 3:
            numero_historia_clinica = int(input("Ingrese el numero de historia " \
            "clinica del paciente que desea buscar: "))
            print(buscar(matriz,numero_historia_clinica))
        case 4:
            print(ordenar(matriz))
        case 5:
            print(mas_dias_internacion(matriz))
        case 6:
            print(menos_dias_internacion(matriz))
        case 7:
            print(mas_5_dias_internacion(matriz))
        case 8:
            print(promedio(matriz))
        case 9:
            print("Finalizando la sesion.")
        case _:
            print("No es un valor correcto de los indicados.")

