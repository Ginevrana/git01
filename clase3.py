# FUNCIONES
# Conjunto de instrucciones que busca resolver un problema específico dentro del programa: divide y organiza el código en partes más simples, y encapsula el código para reutilizarlo y evitar repetirlo dentro del programa

# Principio de reusabilidad:
# Si tenemos un fragmento de código usado en muchos lugares la mejor solucion sería pasarlo a una función y evitar tener código repetido, para actualizarlo en un sólo lugar.

# Principio de modularidad:
# En lugar de extensas líneas de código, mejor crear módulos o funciones que agrupen ciertos fragmentos de código en funcionalidades específicas y mejorando su lectura.

from operator import truediv


def sumar (param1,param2):
    suma = param1+param2
    print (f'Resultado de valores sumados: {suma}')
    
sumar(4,5)

#--------------------------------------------------------------------------------------------------

# CÓMO EJECUTAR FUNCIONES:

def main():
    print('Comienzo de programa')

    multiplica_por_3(7)
    print('Siguiente')

    multiplica_por_3(113)
    print('Fin')

def multiplica_por_3(num):
    print(f'{num}*3={num*3}')

main()

#--------------------------------------------------------------------------------------------------

# Parámetros opcionales o argumentos por defecto
# Asignamos un valor por defecto en caso de no asignarle ninguno

def suma(a, b, c=0):
    return a+b+c

suma(5,5,3) #13
suma(5,5)  #10

#--------------------------------------------------------------------------------------------------
# RETURN VACÍO
# Cuadrado de un número sólo si este es par:
def cuadrado_de_par(numero):
    if not numero % 2 == 0:
        return
    else:
        print (numero**2)

cuadrado_de_par(3)

#--------------------------------------------------------------------------------------------------
# VARIOS RETURN
# La función devuelve True si es par o False de no serlo

def es_par(numero):
    if numero % 2 == 0:
        print (True)
    else:
        print (False)

es_par(7)

#--------------------------------------------------------------------------------------------------
# RETURN DEVUELVE MÁS DE UN VALOR

def cuadrado_y_cubo(numero):
    return numero **2, numero **3

cuad, cubo = cuadrado_y_cubo(4)

print(cuadrado_y_cubo(4))

####

def tabla_del(numero):
    resultados = []
    for i in range (11):
        resultados.append(numero*i)
    return resultados

res = tabla_del(3)

print(res)

#-------------------------------------------------------------------------------------------------------
# Ámbito local de la variable
# Parámetros y variables definidos dentro de una función (ámbito local) no pueden ser utilizados por fuera de ésta porque no searán reconocidos.

def saludo(nombre):
    x = 10
    print(f'Hola {nombre}')

saludo('Gustavo') # Hola Gustavo
print(x) # Error name 'x' is not defined

#-------------------------------------------------------------------------------------------------------

# Ciclo de vida de las variables
# Las variables definidas fuera de una función (global), pueden ser visibles dentro de las funciones donde sólo se puede consultar su valor.
y = 20
def muestra_x():
    x = 10
    print(f'x vale {x}')
    print(f'y vale {y}')

muestra_x()
# x vale 10
# y vale 20