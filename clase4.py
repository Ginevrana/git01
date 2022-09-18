 # LISTAS
 # Son ORDENADAS (mantienen el orden con que fueron creadas), contienen cualquier tipo de dato, se pueden indexar con [i], se pueden ANIDAR una dentro de otra, son MUTABLES (pueden ser modificadas) y son DINÁMICAS (se añaden o eliminan elementos).

 # Lista vacía 
 # []

 # Lista con elementos
 # [1,2,3]

 # Lista con diferentes tipos de elementos
 # ["Python", 2,3]

# VECTORES O ARREGLOS DE UNA DIMENSIÓN
# Es una lista con datos de un mismo tipo

# v = [32,74,92,25,81]
# print(v[0])
# print(v[2])
# print(v[1:4])

# MATRICES O ARREGLOS DE DOS DIMENSIONES
# Es una lista cuyos elementos tienen la misma longitud  y contienen elementos del mismo tipo

a=[[23,45,63],[72,81,91],[56,64,37],[34,75,26]]

# Para acceder a la primer lista
print(a[1])
# Resultado [72, 81, 91]

# Para acceder a una posición específica
print(a[1][2])
# Resultado 91


# MATRICES MULTIDIMENSIONALES
# La lista de python se puede extender y manejar listas en más niveles

mul= [1,[11,22],[[111,222],[333,444]]]

print(mul[0])
# Resultado: 1

print(mul[2])
# Resultado: [[111, 222], [333, 444]]

print(mul[2][1][0])
# Resultado: 333

