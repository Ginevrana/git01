# Ejercicio 1 - Realizar función que se llame area_rectangulo()

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