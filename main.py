"""
Archivo: main.py

El usuario podrá:
- Añadir productos
- Eliminar productos
- Actualizar datos
- Buscar productos
- Visualizar inventario
"""

from inventario import Inventario
from producto import Producto

def menu():
    inventario = Inventario()

    while True:
        print("\n========== SISTEMA DE INVENTARIO ==========")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        # ---------------------------------------
        # AÑADIR PRODUCTO
        # ---------------------------------------
        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")

            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
            except ValueError:
                print("Error: cantidad o precio inválidos.")
                continue

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        # ---------------------------------------
        # ELIMINAR
        # ---------------------------------------
        elif opcion == "2":
            id_producto = input("Ingrese ID a eliminar: ")
            inventario.eliminar_producto(id_producto)

        # ---------------------------------------
        # ACTUALIZAR
        # ---------------------------------------
        elif opcion == "3":
            id_producto = input("Ingrese ID del producto: ")
            cantidad = input("Nueva cantidad (enter si no cambia): ")
            precio = input("Nuevo precio (enter si no cambia): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        # ---------------------------------------
        # BUSCAR
        # ---------------------------------------
        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        # ---------------------------------------
        # MOSTRAR
        # ---------------------------------------
        elif opcion == "5":
            inventario.mostrar_todos()

        # ---------------------------------------
        # SALIR
        # ---------------------------------------
        elif opcion == "6":
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
