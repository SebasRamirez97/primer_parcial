from .matriz_vacia import vacia

def mostrar_todos(matriz):
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion\n"
    else:
        for i in range(len(matriz)):
            print(matriz[i])

def mostrar_paciente_mas_dias_internacion(matriz: list)->str|list:
    """Recibe una matriz, en primer instancia 
    revisa si la matriz esta vacia, en caso de 
    estarlo nos dara un mensaje de matriz vacia. 
    Sino nos devuelve todos los datos del
    paciente con mas dias de internacion.
     
    ### Args:
        matriz: list
    ### Returns:
        str | list
    """
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion\n"
    else:
        maximo = -float("inf")
        mas_dias_internacion = []
        for i in range(len(matriz)):
            if matriz[i][4] > maximo:
                maximo = matriz[i][4]
                mas_dias_internacion = matriz[i]
        '''for i in range(len(matriz)):
            if mas_dias_internacion[0][4] == matriz[i][4]:
                mas_dias_internacion += matriz[i]'''
        return mas_dias_internacion

def mostrar_paciente_menos_dias_internacion(matriz: list)->str|list:
    """Recibe una matriz, en primer instancia 
    revisa si la matriz esta vacia, en caso de 
    estarlo nos dara un mensaje de matriz vacia. 
    Sino nos devuelve todos los datos del
    paciente con menos dias de internacion.
     
    ### Args:
        matriz: list
    ### Returns:
        str | list
    """
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion\n"
    else:
        minimo = float("inf")
        menos_dias_internacion = []
        for i in range(len(matriz)):
            if matriz[i][4] < minimo:
                minimo = matriz[i][4]
                menos_dias_internacion = matriz[i]
        '''for i in range(len(matriz)):
                if menos_dias_internacion[0][4] == matriz[i][4]:
                    menos_dias_internacion += matriz[i]'''
        return menos_dias_internacion
    
def mostrar_mayor_5_dias_internacion(matriz: list)->str|list:
    """Recibe una matriz, en primer instancia 
    revisa si la matriz esta vacia, en caso de 
    estarlo nos dara un mensaje de matriz vacia. 
    En el caso de haber pacientes con mas de 5 dias de internacion devuelve
    la cantidad, en el caso de no haber devuelve un mensaje de no hay pacientes
    con mas de 5 dias de internacion.
     
    ### Args:
        matriz: list
    ### Returns:
        str | int

    """
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion\n"
    else:
        cantidad = 0
        for i in range(len(matriz)):
            if matriz[i][4] < 5:
                cantidad += 1
        if cantidad == 0:
            return "No hay pacientes con mas de 5 dias de internacion"
        else:
            return cantidad