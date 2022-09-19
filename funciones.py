# Ejercicio 1 - Realizar función que se llame area_rectangulo()

from xml.dom.minidom import ReadOnlySequentialNamedNodeMap


def area_rectangulo(x,y):
    return x*y

print(f'El área del rectangulo es: {area_rectangulo(5,2)}')

# Ejercicio 2 - Realizar función que se llame area_circulo()

def area_circulo(radio):
    pi= 3.14159
    return pi * (radio ** 2)

print(f'El área del circulo es: {area_circulo(2)}')

# Ejercicio 3 - Realizar función que se llame relación

def relacion(x,y):
    if x>y:
        return 1
    elif x<y:
        return -1
    elif x==y:
        return 0

print(relacion(5,5))

# Ejercicio 4 - Realizar función que se llame intermedio ()

def intermedio(a,b):
    resultado = a+b
    return resultado/2

print(f'El Nº intermedio es: {intermedio(56,84)} ')


# Ejercicio 5 - Realizar una función que se llame recortar()

def recortar(a,b,c):
    if a<b:
        return b
    elif a>c:
        return c
    else:
        return a

print(recortar(7,6,9))


# Ejercicio 6 - Realizar funcion que se llame separar ()
lista=[1,58,36,97,45,61,2,86]

def separar():
    pares=[]
    impares=[]
    for i in lista:
        if (i%2==0):
            pares.append(i)
        else:
            impares.append(i)
        return pares.sort(), impares.sort()

pares, impares = separar()

print(pares,impares)