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
        print("El número ingresado es impar")
    else:
        print(input("Ingrese un número impar: "))
    print("Próxima instrucción")


# Ejercicio 2
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

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

    while (email == "@"):
        if (email == "@"):
            print("La información ingresada es un mail")
            break
        else:
            print("La información ingresada no es un mail")
            break


# Ejercicio 4

    verduleria = (["manzanas", "peras", "naranjas"])
    for i in verduleria(0, len(i)):
        resultado = i + 1
        print (resultado)


# Ejercicio 6

    lista=[5,34,81,27,19]
    contador=0
    numeros=0
    for i in lista:
        contador = contador + i

    for i in lista:
        numeros = numeros + i

    promedio = contador / numeros
    print(promedio)

if __name__ == '__main__':
    main()
