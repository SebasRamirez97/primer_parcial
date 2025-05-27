from .matriz_vacia import vacia

def mostrar_todos(matriz: list)->None:
    '''Recibe una matriz. En primer instancia revisa si la matriz esta vacia, en caso de 
    estarlo imprimira un mensaje de matriz vacia.
    Sino nos imprimira todos los datos de la matriz.
    
    ###Argas:
        matriz: list
    ###Returns:
        None
    '''
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion\n"
    else:
        for i in range(len(matriz)):
            print(matriz[i])

def mostrar_paciente_mas_dias_internacion(matriz: list)->None:
    """Recibe una matriz, en primer instancia 
    revisa si la matriz esta vacia, en caso de 
    estarlo nos dara un mensaje de matriz vacia. 
    Sino nos imprira todos los datos del
    paciente con mas dias de internacion, 
    en el caso de haber mas de uno con la 
    cantidad maxima igual se imprimiran ambos.
    
     
    ### Args:
        matriz: list
    ### Returns:
        None
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
       
        nueva_mas_dias_internacion = []
        nueva_mas_dias_internacion += [mas_dias_internacion] 
        
        for i in range(len(matriz)):
            if nueva_mas_dias_internacion[0][4] == matriz[i][4] and nueva_mas_dias_internacion[0][0] != matriz[i][0]:
                nueva_mas_dias_internacion += [matriz[i]]
        
        mostrar_todos(nueva_mas_dias_internacion)

def mostrar_paciente_menos_dias_internacion(matriz: list)->None:
    """Recibe una matriz, en primer instancia 
    revisa si la matriz esta vacia, en caso de 
    estarlo nos dara un mensaje de matriz vacia. 
    Sino nos imprira todos los datos del
    paciente con mas dias de internacion, 
    en el caso de haber mas de uno con la 
    cantidad minima igual se imprimiran ambos.
     
    ### Args:
        matriz: list
    ### Returns:
        None
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
        
        nueva_menos_dias_internacion = []
        nueva_menos_dias_internacion += [menos_dias_internacion] 
        
        for i in range(len(matriz)):
            if nueva_menos_dias_internacion[0][4] == matriz[i][4] and nueva_menos_dias_internacion[0][0] != matriz[i][0]:
                nueva_menos_dias_internacion += [matriz[i]]
        
        mostrar_todos(nueva_menos_dias_internacion)

    
def mostrar_mayor_5_dias_internacion(matriz: list)->str|list:
    """Recibe una matriz, en primer instancia 
    revisa si la matriz esta vacia, en caso de 
    estarlo nos dara un mensaje de matriz vacia. 
    Sino en el caso de haber pacientes con mas de 5 dias de internacion devuelve
    la cantidad, en el caso de no haber devuelve un mensaje de no hay pacientes
    con mas de 5 dias de internacion.
     
    ### Args:
        matriz: list
    ### Returns:
        str | int

    """
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion.\n"
    else:
        cantidad = 0
        for i in range(len(matriz)):
            if matriz[i][4] > 5:
                cantidad += 1
        
        if cantidad == 0:
            return "No hay pacientes con mas de 5 dias de internacion.\n"
        else:
            return f"La cantidad de pacientes con mas de 5 dias de internacion son {cantidad}.\n"