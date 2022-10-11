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

####-------------------------------------------------------------------------
#### Ordenamiento rápido, se ordena desde el elemento del medio y subdivide la lista entre mayores y menores.
##
##def quicksort(lista,primero,ultimo):
##    ## Las variables izquierda y derecha se utilizan para barrer la lista desde la izquierda a derecha y de derecha a izquierda respectivamente.
##    izquierda = primero
##    derecha = ultimo-1
##    ## pivote almacena el índice del elemento a ordenar para separar la lista en dos sublistas.
##    pivote = ultimo
##    ## La sublista de la izquierda tendrá los elementos menores al elemento en la posición pivote y en la sublista derecha los elementos mayores.
##
##    while(izquierda<derecha):
##        ## Cuando el elemento de la lista en la posición izquierda es menor que el pivote se incrementa el índice izquierda.
##        while(lista[izquierda]<lista[pivote]) and (izquierda<=derecha):
##            izquierda+=1
##
##        ## Si el elemento de la lista en la posición derecha es mayor que el elemento en la posición pivote se decrementa el índice derecha.
##        while (lista[derecha]>lista[pivote]) and (derecha>=izquierda):
##            derecha-=1
##
##        ## Cuando estos dos ciclos se detienen, si el índice izquierda es menor que la derecha significa que deben intercambiar valores almacenados en esos índices.
##        if(izquierda<derecha):
##            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
##        ## Luego se continúa con el ciclo while para terminar de reubicar los valores menores y mayores.
##
##    ## Cuando se finaliza el intercambio de elementos, se procede a ubicar el elemento pivote a su posición final en la lista izquierda (quedando ya ordenado). De esta manera queda dividida la lista en dos sublistas parcialmente ordenadas.
##    if (lista[pivote]<lista[izquierda]):
##        lista[izquierda], lista[pivote] = lista [pivote], lista[izquierda]
##
##    ## Finalmente se evalúa si las sublistas izquierda y derecha tienen elementos para ordenar. De ser así se llama recursivamente a la función quicksort actualizando los parámetros primero y último.
##    if (primero < izquierda):
##        quicksort(lista, primero, izquierda-1)
##
##    if (ultimo > izquierda):
##        quicksort(lista, izquierda+1, ultimo)
##    ## Esto particiona la lista en sublistas hasta que las sublistas ya no puedan ser particionadas y queden ordenadas.
##
##
##print(lista)
##quicksort(lista, 0, len(lista)-1)
##print(lista)

####-------------------------------------------------------------------------

## Ordenamiento por mezcla. Si el tamaño de la lista es uno o menor la lista está ordenada, sino se divide la lista en dos sublistas de la mitad del tamaño de la lista y se llama recursivamente a ordenar las sublistas usando ordenamiento por mezcla.
## Por último se mezclan las sublistas ordenadas en una sola lista. Ordenar una lista pequeña es más rápido que ordenar una lista grande, y construir una lista ordenada a partir de dos listas ordenadas también es una actividad rápida.

##def mergesort(lista):
##    ## Se verifica si el tamaño de la lista es menor o igual a uno, condición de fin de las llamadas recursivas y devuelve la lista
##    if (len(lista)<=1):
##        return lista
##
##    ## Sino se calcula el valor del índice medio dividiendo la cantidad de elementos de la lista dividido por dos (división entera) para comenzar a dividir la lista.
##    else:
##        medio = len(lista) // 2
##        izquierda = []
##
##        ## Se generan las listas izquierda y derecha. Luego se utilizan dos ciclos for para cargar los elementos.
##        for i in range (0,medio):
##            izquierda.append(lista[i])
##
##        derecha = []
##
##        for i in range (medio, len(lista)):
##            derecha.append(lista[i])
##
##        ## Luego se llama recursivamente a mergesort() con las sublistas izquierda y derecha, asignando los resultados en las mismas variables.
##        izquierda = mergesort(izquierda)
##        derecha = mergesort(derecha)
##
##        ## Una vez que ya no pueden ser particionadas (fin de recursividad) y cada una de estas se considerean ordenadas comienza el proceso de combinación de dichas sublistas.
##        if(izquierda[medio-1] <= derecha [0]):
##            izquierda += derecha
##
##            return izquierda
##
##        ## Si el último elemento de la sublista izquierda es menor o igual que el primero de la sublista derecha, se concatena la sublista derecha al final de la izquierda.
##        resultado = merge(izquierda, derecha)
##        ## Dado que ambas sublistas están ordenadas, entonces todos los elementos de la sublista derecha son mayores o iguales que los de la sublista izquierda.
##        return resultado
##
##
##def merge (izquierda, derecha):
##    ## Esta función se encarga de mezclar dos listas que ya se encuentran ordenadas.
##    ## Para esto se crea una lista vacía
##    lista_mezclada=[]
##
##    ## Y utilizamos un ciclo while siempre que las dos sublistas tengan al menos un elemento
##    while(len(izquierda)>0) and (len(derecha)>0):
##
##        ## Se define qué elemento es menor, el primero de la sublista izquierda o el de la sublista derecha y luego se quita una sublista y se agrega a la otra.
##        if (izquierda[0]<derecha[0]):
##            lista_mezclada.append(izquierda.pop(0))
##        else:
##            lista_mezclada.append(derecha.pop(0))
##
##    ## Cuando finaliza el ciclo while significa que una de las dos sublistas está vacía y la otra aún tiene elementos.
##    ## La sublista que aún tiene elementos se concatena al final de la lista creada y finalmente se retorna la lista que contiene las dos sublistas ordenadas.
##    if(len(izquierda)>0):
##        lista_mezclada += izquierda
##
##    if(len(derecha)>0):
##        lista_mezclada+=derecha
##
##    return lista_mezclada
##
##print(lista)
##mergesort(lista)
##print(lista)

####-------------------------------------------------------------------------
##--------------------- ALGORITMO DE BÚSQUEDA -------------------------------
####-------------------------------------------------------------------------

## Siempre es necesario buscar un elemento para poder determinar si está presente o no dentro de nuestro conjunto de datos.
## Cone stos se podría saber si un determinado elemento está en una estructura de datos o no y determinar qué actividades podrían realizarse: inserción en el caso de no estar y modificación o eliminación en caso de estar
## Estos métodos al igual que los de ordenamiento suelen aplicarse sobre vectores, en nuestro caso usaremos listas.

####-------------------------------------------------------------------------
## Búsqueda secuencial
## Este es el algoritmo de búsqueda más simple. Compara secuencialmente el elemento buscado con cada elemento de la lista.

## El elemento buscado puede existir o no dentro de la lista y la única forma de poder determinarlo es recorrer la lista completa.

##def secuencial(lista, buscado):
##    ## Inicialmente se asigna -1 a la variable posición para indicar que el elemento buscado no ha sido encontrado.
##    posicion = -1
##
##    ## Con un ciclo for de 0 a la cantidad de elementos de la lista, recorremos todos los elementos de la lista y verificamos si el elemento buscado es igual al elemento de la lista en la posición de la variable de control lista [i]
##    for i in range (0, len(lista)):
##        if (lista[i] ==buscado):
##            posicion = i
##            ## Si la lista tiene 10 mil elemento y el elemento buscado esta en la posición 50, el ciclo debería detenerse para no recorrer los 9950 restantes. Entonces podríamos detener el ciclo for con una instrucción de break cuando se encuentra el elemento buscado.
##            break
##
##    ## Si la comparación es True significa que se encontró el elemento buscado y asignamos a la variable posición el valor de la variable i, que es la posición donde fue encontrado.
##    return posicion
##
##    ## Al finalizar el ciclo for retornamos la variable posicion, que si aún tiene valor -1 significa que el elemento buscado no se encuentra dentro de la lista, sino indicará la posición donde fue encontrado.

##print(lista)
##print(secuencial(lista,8))

####-------------------------------------------------------------------------
## Para no romper el funcionamiento de un ciclo, podríamos usar un ciclo while en lugar de un for evitando usar la sentencia break.

##def centinela(lista, buscado):
##    posicion =-1
##    i=0
##
##    ## Le agregamos una condicion extra, que la variable posicion sea igual a -1 que nos indica que el elemento buscado aún no ha sido encontrado.
##    while(i<len(lista)) and (posicion == -1):
##        if(lista[i] == buscado):
##            posicion = i
##
##        i+=1
##
##    return posicion
##
##print(lista)
##print(centinela(lista, 811))

####-------------------------------------------------------------------------
## Búsqueda binaria: Este algoritmo también llamado "búsqueda logarítmica" es muy eficiente en cuanto al número de comparaciones requeridas para determinar si un elemento existe o no dentro de una lista de elementos.
## Tiene un requisito no excluyente para que funcione: la lista de elementos debe estar ordenada.

## Su principio de funcionamiento se basa en determinar si el elemento buscado se encuentra en medio de la lista dividiendo la lista en dos sublistas, la izquierda y la derecha.

## Si el elemento buscado no está en el medio, dependiendo si es menor o mayor, se repite el mismo procedimiento con la sublista izquierda o la derecha descartando la otra.

## Este procedimiento se repite mientras las sublistas puedan ser particionadas o se encuentre el elemento buscado descartando una sublistas en cada particion, esto hace que este algoritmo sea muy eficiente.

def binaria(lista, buscado):
    ## Primero se asigna -1 a la variable posición para indicar que el elemento buscado no ha sido encontrado
    posicion=-1
    primero=0
    ## También se asignan a la variable primero el índice 0 y a último el numero de elementos de la lista-1
    ultimo=len(lista)-1

    ## Luego se usa un ciclo while con la condición que el índice primero sea menor o igual que el índice último (para que aún se puede particionar o buscar en las sublistas) y que aún no se haya encontrado el elemento buscado.
    while(primero<=ultimo) and (posicion ==-1):
        ## Se calcula el valor del índice medio de la lista, sumando los valores de primero y último, y dividiendo el resultado por dos(división entera).
        medio = (primero + ultimo)//2

        ## Se verifica si el elemento en el medio de la lista es igual al busscado, de ser así se le asigna el valor de medio a posicion, sino se procede a particionar la lista actualizando los índices primero o último, y descartando el resto de la lista
        if (lista[medio]==buscado):
            posicion=medio
        else:
            ## Si el elemento buscado es menor que el valor de la lista en la posición medio se actualiza el índice último asignándole el valor de medio-1, sino se actualiza primero con el valor medio +1
            if(buscado<lista[medio]):
                ultimo=medio-1

            else:
                primero = medio + 1

    ## Finalmente se devuelve el valor de posicion apra poder determinar si el elemento fue encontrado o no.
    return posicion

print(lista)
print(binaria(lista,7))