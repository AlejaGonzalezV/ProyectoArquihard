from ProyectoFinal import Algoritmos

def start():
    alg = Algoritmos()

    print("Inserte la versión del algoritmo")
    version = input()

    src = "./img/im1.bmp"

    if version == 1:
        alg.algoritmoV1(src)
    elif version == 2:
        alg.algoritmoV2(src)
    elif version == 3:
        alg.algoritmoV3(src)
    elif version == 4:
        alg.algoritmoV4(src)
    elif version == 5:
        alg.algoritmoV5(src)
    else:
        print("Ingrese una opción válida")