from funciones.cargar_pacientes import ingreso_pacientes as carga
from funciones.mostrrar_segun import mostrar_todos as todos
from funciones.busqueda_por_historia import buscar_paciente as buscar
opcion = 0
matriz = []
while(opcion != 9):
    print("MENU PRINCIPAL")
    print("1. Carga pacientes.\n" \
    "2. Mostrar todos los pacientes.\n" \
    "3. Buscar pacientes por numero de historia clinica.\n" \
    "4. Ordenar pacientes por numero de historia clinica.\n" \
    "5. Mostrar pacientes con mas dias de internacion.\n" \
    "6. Mostrar pacientes con menos dias de ibnternacion.\n" \
    "7. Cantidad de pacientes con mas de 5 dias de internacion.\n" \
    "8. Promedio de dias de internacion de todos los pascientes." \
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
            "clinica del paciente que desea buscar"))
            buscar(matriz,numero_historia_clinica)
        case 4:
            pass