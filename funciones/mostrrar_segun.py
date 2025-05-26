from .matriz_vacia import vacia

def mostrar_todos(matriz):
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion\n"
    else:
        for i in range(len(matriz)):
            print(matriz[i])