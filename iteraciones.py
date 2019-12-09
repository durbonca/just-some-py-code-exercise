""" def imprimir(cadena):
    for i in range (0,len(cadena)):
        print (cadena[i])
        print('')


if __name__ == "__main__":
    cadena = str(input("escribir cadena: "))
    imprimir(cadena) """

def imprimir(cadena):
    for i in cadena:
        print (i)
        print('')


if __name__ == "__main__":
    cadena = str(input("escribir cadena: "))
    imprimir(cadena)