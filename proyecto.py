import json
from funcion import *
 

 
def main():
    filename = "productos.txt"
    productos = cargar_productos(filename)
    
    while True:
        print("Seleccione una opción:")
        print("1. Ingresar Productos")
        print("2. Imprimir productos")
        print("3. Buscar Producto")
        print("4. Editar Producto")
        print("5. Eliminar Producto")
        opcion1 = int(input(">> "))
        
        if opcion1 == 1:
            ingresar_productos(productos)
            guardar_productos(filename, productos)
        elif opcion1 == 2:
            imprimir_productos(productos)
        elif opcion1 == 3:
            nombre = input("Ingrese el nombre del producto a buscar: ")
            indices = buscar_producto_por_nombre(productos, nombre)
            imprimir_producto_por_index(productos, indices)
        elif opcion1 == 4:
            editar_producto(productos)
            guardar_productos(filename, productos)
        elif opcion1 == 5:
            eliminar_producto(productos)
            guardar_productos(filename, productos)
        else:
            print("Opción no válida .")
        
        opcion2 = int(input("¿Desea elegir una nueva opción? 1. Sí / 2. No\n>> "))
        if opcion2 != 1:
            break
 
if __name__ == "__main__":
    main()
