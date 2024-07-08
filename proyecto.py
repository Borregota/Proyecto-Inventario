import json
 
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
 
def cargar_productos(filename):
    try:
        with open(filename, 'r') as file:
            productos = json.load(file)
            return [Producto(p['nombre'], p['cantidad'], p['precio']) for p in productos]
    except FileNotFoundError:
        print("Error al abrir el archivo para cargar.")
        return []
 
def guardar_productos(filename, productos):
    with open(filename, 'w') as file:
        json.dump([p.__dict__ for p in productos], file)
 
def ingresar_productos(productos):
    cantidad = int(input("Ingrese la cantidad de productos que desea ingresar: "))
    for _ in range(cantidad):
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = float(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        productos.append(Producto(nombre, cantidad, precio))
 
def imprimir_productos(productos):
    print("N.producto\tCantidad\tPrecio")
    for p in productos:
        print(f"{p.nombre}\t\t{p.cantidad}\t\t{p.precio}")
 
def buscar_producto_por_nombre(productos, nombre):
    return [i for i, p in enumerate(productos) if p.nombre == nombre]
 
def imprimir_producto_por_index(productos, indices):
    if not indices:
        print("No se encontró ningún producto.")
        return
    print("N.producto\tCantidad\tPrecio")
    for index in indices:
        p = productos[index]
        print(f"{p.nombre}\t\t{p.cantidad}\t\t{p.precio}")
 
def editar_producto(productos):
    nombre = input("Ingrese el nombre del producto que desea editar: ")
    indices = buscar_producto_por_nombre(productos, nombre)
    if not indices:
        print("El producto ingresado no existe.")
        return
    imprimir_producto_por_index(productos, indices)
    opcion = int(input("Seleccione el número del producto que desea editar: ")) - 1
    if opcion < 0 or opcion >= len(indices):
        print("Opción no válida.")
        return
    index = indices[opcion]
    nueva_cantidad = float(input("Ingrese la nueva cantidad: "))
    nuevo_precio = float(input("Ingrese el nuevo precio: "))
    productos[index].cantidad = nueva_cantidad
    productos[index].precio = nuevo_precio
 
def eliminar_producto(productos):
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")
    indices = buscar_producto_por_nombre(productos, nombre)
    if not indices:
        print("El producto ingresado no existe.")
        return
    imprimir_producto_por_index(productos, indices)
    opcion = int(input("Seleccione el número del producto que desea eliminar: ")) - 1
    if opcion < 0 or opcion >= len(indices):
        print("Opción no válida.")
        return
    index = indices[opcion]
    productos.pop(index)
 
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
            print("Opción no válida.")
        
        opcion2 = int(input("¿Desea elegir una nueva opción? 1. Sí / 2. No\n>> "))
        if opcion2 != 1:
            break
 
if __name__ == "__main__":
    main()
 