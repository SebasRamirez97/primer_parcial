from .matriz_vacia import vacia

def ordenar_pacientes_ascendente(matriz: list)->list:
    """Recibe una matriz, en primer instancia 
    revisa si la matriz esta vacia, en caso de 
    estarlo nos dara un mensaje de matriz vacia. 
    Sino nos ordena la matriz segun el precio de 
    manera ascendente y la devuelve.
    
    ### Args:
        matriz: list
    ### Returns:
        list
    """
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion\n"
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz)-i-1):
                if matriz[j][0] > matriz[j+1][0]:
                    aux = matriz[j+1]
                    matriz[j+1] = matriz[j]
                    matriz[j] = aux

        return matriz