## Clase 5 Búsqueda y ordenamiento
## Algoritmos de ordenamiento
## Para saber si contiene un elemento y ordenarlos de distintas maneras

## MÉTODO BURBUJA
## Se comparan los elementos de la lista uno por uno y se van corriendo del lugar según el orden deseado.


lista = [56,7,11,45,81]

def burbuja(lista):
    for i in range (0, len(lista)-1):
        for j in range(0, len(lista)-i-1):
            if(lista[j]>lista[j+1]):
                lista[j],lista[j+1] = lista[j+1],lista[j]

burbuja(lista)
print(lista)


def burbuja(arreglo):
    # Calculamos la longitud del arreglo para tener un código más limpio
    longitud = len(arreglo)
    # Recorremos todo el arreglo
    for i in range(longitud):
        # Dentro del ciclo, volvemos a recorrerlo. Pero ahora hasta el penúltimo elemento
        for indice_actual in range(longitud - 1):
            indice_siguiente_elemento = indice_actual + 1
            # Si el actual es mayor que el siguiente, ...
            # Nota: para un orden inverso, cambia `>` por `<`
            if arreglo[indice_actual] > arreglo[indice_siguiente_elemento]:
                # ... intercambiamos los elementos
                arreglo[indice_siguiente_elemento], arreglo[indice_actual] = arreglo[indice_actual], arreglo[indice_siguiente_elemento]
    # No hace falta regresar nada, pues el arreglo ya fue modificado


# Modo de uso.
mi_arreglo = [3, 4, 1, 2, 3, 7, 55, 34, 43, 3]
print("Original: ")
print(mi_arreglo)
burbuja(mi_arreglo)
print("Ordenado: ")
print(mi_arreglo)