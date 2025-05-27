from .matriz_vacia import vacia

def promedio_pacientes(matriz)->float:
    '''Recibe un matriz. En primer instancia revisa 
    si la matriz esta vacia, en caso de 
    estarlo imprimira un mensaje de matriz vacia.
    Sino devuelve el promedio de 
    cantidad de dias de internacion de los pacientes.
    
    ###Ars:
        matriz: list
    ###Return:
        float
    '''
    
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion\n"
    else:
        sumatoria = 0
        cantidad_pacientes = len(matriz)
        for i in range(cantidad_pacientes):
            sumatoria += matriz[i][4]
        
        promedio = sumatoria / cantidad_pacientes

    return promedio