## Clase 5 Búsqueda y ordenamiento
## Algoritmos de ordenamiento
## Para saber si contiene un elemento y ordenarlos de distintas maneras

## MÉTODO BURBUJA
## Se comparan los elementos de la lista uno por uno y se van corriendo del lugar según el orden deseado.


lista = [56,7,11,45,81,358,462,129,456,812]
##
##def burbuja(lista):
##    for i in range (0, len(lista)-1):
##        for j in range(0, len(lista)-i-1):
##            if(lista[j]>lista[j+1]):
##                lista[j],lista[j+1] = lista[j+1],lista[j]
##
##burbuja(lista)
##print(lista)
##
##
##def burbuja(arreglo):
##    # Calculamos la longitud del arreglo para tener un código más limpio
##    longitud = len(arreglo)
##    # Recorremos todo el arreglo
##    for i in range(longitud):
##        # Dentro del ciclo, volvemos a recorrerlo. Pero ahora hasta el penúltimo elemento
##        for indice_actual in range(longitud - 1):
##            indice_siguiente_elemento = indice_actual + 1
##            # Si el actual es mayor que el siguiente, ...
##            # Nota: para un orden inverso, cambia `>` por `<`
##            if arreglo[indice_actual] > arreglo[indice_siguiente_elemento]:
##                # ... intercambiamos los elementos
##                arreglo[indice_siguiente_elemento], arreglo[indice_actual] = arreglo[indice_actual], arreglo[indice_siguiente_elemento]
##    # No hace falta regresar nada, pues el arreglo ya fue modificado
##
##
### Modo de uso.
##mi_arreglo = [3, 4, 1, 2, 3, 7, 55, 34, 43, 3]
##print("Original: ")
##print(mi_arreglo)
##burbuja(mi_arreglo)
##print("Ordenado: ")
##print(mi_arreglo)


##------------------------------------------------------------------------

##def burbuja_mejorado(lista):
    ##i=0
    ##control=True

    ##while(i<=len(lista)-2) and control:
        ##control = False
        ##for j in range(0,len(lista-i-1))






##-------------------------------------------------------------------------
##def coctel(lista):
##    izquierda=0
##    derecha=len(lista)-1
##    control = True
##
##    while(izquierda<derecha) and control:
##        control = False
##
##        for i in range(izquierda, derecha):
##            if (lista[i]>lista[i+1]):
##                control=True
##                lista[i],lista[i+1] =lista[i+1], lista[i]
##
##        derecha-= 1
##
##        for j in range(derecha, izquierda, -1):
##            if (ilsta[j]<lista[j-1]):
##                control = True
##                lista[j], lista[j-1] = lista[j-1], lista[j]
##
##        izquierda +=1

##-------------------------------------------------------------------------
## Ordenamiento por selección - recorre iterativamente la lista de elementos en busca del menor, luego lo selecciona para ubicarlo a la izquierda de la lista pero tambien se puede buscar el mayor y moverlo a la derecha

##def seleccion(lista):
##    for i in range(0, len(lista)-1):
##        minimo = i
##        for j in range(i+1, len(lista)):
##            if(lista[j]<lista[minimo]):
##                minimo = j
##
##        lista[i], lista[minimo] = lista[minimo], lista[i]
##
##print(lista)
##seleccion(lista)
##print(lista)

##Resultado:
##[56, 7, 11, 45, 81, 358, 462, 129, 456, 812]
##[7, 11, 45, 56, 81, 129, 358, 456, 462, 812]

##-------------------------------------------------------------------------
## Ordenamiento por inserción se usan dos ciclos for

##def insercion(lista):
##    for i in range(1,len(lista)+1):
##        k = i-1
##        while(k>0) and (lista[k]<lista[k-1]):
##            lista[k], lista[k-1] = lista[k-1], lista[k]
##            k-=1
##
##
##print(lista)
##insercion(lista)
##print(lista)

##-------------------------------------------------------------------------
## Ordenamiento rápido, se ordena desde el elemento del medio y subdivide la lista entre mayores y menores

##def quicksort(lista,primero,ultimo):
##    izquierda = primero
##    derecha = ultimo -1
##    pivote = ultimo
##
##    while(izquierda<derecha):
##        while(lista[izquierda]<lista[pivote]) and (izquierda<=derecha):
##            izquierda+=1
##
##        while (lista[derecha]>lista[pivote]) and (derecha>=izquierda):
##            derecha-=1
##
##        if(izquierda<derecha):
##            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
##
##        if (lista[pivote]<lista[izquierda]):
##            lista[izquierda], lista[pivote] = lista [pivote], lista[izquierda]
##
##        if (primero < izquierda):
##            quicksort(lista, primero, izquierda-1)
##
##        if (ultimo < izquierda):
##            quicksort(lista, izquierda+1, ultimo)
##
##print(lista)
##quicksort(lista)
##print(lista)

