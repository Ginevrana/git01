#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      inap
#
# Created:     30/08/2022
# Copyright:   (c) inap 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Flujo condicional I

def main():

    a=3

        if (a < 4):
            print(a)

    print("Próxima instrucción")


# Flujo condicional II
    b=3
        if (b < 4):
            print(a)
        else:
            print("No es menor a 4")

    print("Próxima instrucción")


# Flujo condicional III
    c=3
        if (c =< 4):
            print(a)
        elif (c == 5):
            print("Es igual a 5")
        else:
            print("Es mayor a 5")

    print("Próxima instrucción")

#-------------------------------------------------------------------------------

# Blucles, pueden ser determinados o indeterminados y se utiliza for y while

    d=6

    while (d > 0):
        print(f'Número {a}!')
        d = d - 1

    print("Próxima instrucción")


#-------------------------------------------------------------------------------

# Do while - ejecutará el fragmento de codigo al menos una vez y luego comprobará si la condición se cumple para la siguiente iteración

    palabra_secreta = "python"
    contador = 0

    while True:
        palabra = input("Ingrese palabra secreta: ").lower()
        contador = contador + 1
        if palabra == palabra_secreta:
            break
        if palabra != palabra_secreta and contador > 7:
            break

    print ('Próxima instrucción')

#-------------------------------------------------------------------------------

# For - a diferencia del while - tiene la cantidad de vueltas definidas por el elemento a recorrer

    # for item in elemento_a_recorrer:
        # Cuerpo del bucle
        # Instrucción 1
        # Instrucción 2
        # Instrucción 3

    a = "manzanas"

    for caracter in a:
        print (caracter)

    print ("Próxima instrucción")

# Imprimir según rangos
    a = "bananas"
    for i in range(0, len(a)):
        print(a[i])

    print("Próxima instrucción")


#-------------------------------------------------------------------------------

# Break, sirve para salir del bucle en medio de una iteración
    a = "peras"
    for letra in a:
        print(letra)
        if letra == "n":
            break

#-------------------------------------------------------------------------------

# Continue, sirve para saltar a la próxima iteración

    n = "manzanas"
    for letra in a:
        if letra == "z":
            continue
        print(letra)

    print("Próxima instrucción")

#-------------------------------------------------------------------------------


if __name__ == '__main__':
    main()