lista=[]
promedio=[]
total_ventas=[]

def solicitar(lista):
    suc_id=input("Ingrese ID de sucursal: ")
    if (suc_id != 0):
        nombre=input("Ingrese nombre de sucursal: ")
        ventas=int(input("Ingrese cantidad de ventas: "))
        suc_total=int(input("Ingrese venta total de sucursal: "))
        suc_promedio=suc_total/ventas

        lista.append(suc_id)
        lista.append(nombre)
        lista.append(ventas)
        lista.append(suc_total)
        promedio.append(suc_promedio)
        total_ventas.append(suc_total)
        solicitar(lista)
    else:
        return

    def imprimir(lista):
        print('Los datos ingresados son: ', lista)
        print('Los promedios de venta son: ', promedio)


    def sumar_ventas(total_ventas):
        total = 0
        for i in total_ventas:
            total = total + i
        print('El total vendido por toda la cadena es: ', total)

    if (lista!=[]):
        imprimir(lista)
        sumar_ventas(total_ventas)

solicitar(lista)
imprimir(lista)
sumar_ventas(lista)
