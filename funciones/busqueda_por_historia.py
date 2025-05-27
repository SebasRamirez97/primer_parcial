from .matriz_vacia import vacia

def buscar_paciente(matriz: list,nunmero_historia_clinica: int)->list|str: 
    """Recibe una matriz y un numero de historia clinica.
    En primer instancia revisa si la matriz esta vacia, en caso de 
    estarlo imprimira un mensaje de matriz vacia. 
    Revisara si algun paciente coincide con el numero de historia clinica 
    en el caso de existir nos devolvera la informacion del paciente.
    En caso de no existir nos devolvera un mensaje de paciente no encontrado.
     
    ### Args:
        matriz: list
        numero_historia_clinica: int
    ### Returns:
        str | list
    """
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion.\n"
    else:
        for i in range(len(matriz)):
            if(matriz[i][0] == nunmero_historia_clinica):
                return matriz[i]
            
        return "No se encontro el paciente.\n"