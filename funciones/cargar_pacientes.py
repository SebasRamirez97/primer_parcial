def ingreso_pacientes(matriz:list, cantidad: int)->None:
    """Recibe una matriz y la cantidad de datos que se desea ingresar.
    Luego nos hara llenar cada posicion de la matriz
    con los diferentes datos correspondiente al paciente
        
    ### Args:
        matriz: list
        cantidad :int
    ### Returns:
        None
    """
    for i in range(cantidad):
        numero_historia_clinica = int(input("Ingrese el numero de historia clinica: "))
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        diagnostico = input("Ingrese el diagnostico del paciente")
        cantidad_dias_internacion = int("Ingrese la cantidad de dias de internacion del paciente:")

        matriz += [[numero_historia_clinica,nombre,edad,diagnostico,cantidad_dias_internacion]]