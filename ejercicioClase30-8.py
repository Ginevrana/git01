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

# Ejercicio 1
def main():
    pass

    impar = input("Ingrese un número impar: ")

    if (int(impar) % 2):
        print(input("Ingrese un número impar: "))
    else:
        print("El número ingresado es impar")
    print("Próxima instrucción")


# Ejercicio 2
    numero1 = input("Ingrese el primer número: ")
    numero2 = input("Ingrese el segundo número: ")

    print("1. Sumar, 2. restar y 3. multiplicar")

    operacion = int(input("Ingrese el número de operacion que quiera realizar: "))

    if(operacion == 1):
        suma = numero1 + numero2
        print(f'El resultado de la suma es {suma}')
    elif(operacion == 2):
        resta = numero1 - numero2
        print (f'El resultado de la resta es {resta}')
    elif (operacion == 3):
        multip = numero1 * numero2
        print (f'El resultado de la multiplicación es {multip}')

    print("Próxima instrucción")


# Ejercicio 3
    email = input("Ingrese su mail: ")

    while (email):
        if (email != "@"):
            print("La información ingresada no es un mail")
        else:
            print("La información ingresada es un mail")


# Ejercicio 4

    verduleria = (["manzanas", "peras", "naranjas"])


if __name__ == '__main__':
    main()