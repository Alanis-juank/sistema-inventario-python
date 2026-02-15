
Estructura de datos utilizada:
Lista de objetos tipo Producto.
"""

from producto import Producto

class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.

        Se inicializa una lista vacía que almacenará objetos Producto.
        """
        self.productos = []

    # ------------------------------------------------
    # MÉTODO PARA AÑADIR PRODUCTOS
    # ------------------------------------------------

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario.

        Regla importante:
        El ID del producto debe ser único.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return

        self.productos.append(producto)
        print("Producto añadido correctamente.")

    # ------------------------------------------------
    # ELIMINAR PRODUCTO
    # ------------------------------------------------

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario mediante su ID.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return

        print("Producto no encontrado.")

    # ------------------------------------------------
    # ACTUALIZAR PRODUCTO
    # ------------------------------------------------

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Permite actualizar los datos de un producto.

        Parámetros opcionales:
        cantidad : nueva cantidad
        precio : nuevo precio
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)

                if precio is not None:
                    p.set_precio(precio)

                print("Producto actualizado correctamente.")
                return

        print("Producto no encontrado.")

    # ------------------------------------------------
    # BUSCAR POR NOMBRE
    # ------------------------------------------------

    def buscar_por_nombre(self, nombre):
        """
        Busca productos por coincidencia de nombre.

        Se permite coincidencia parcial:
        Ej: "lap" encontrará "laptop".
        """
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

        if encontrados:
            print("\nProductos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    # ------------------------------------------------
    # MOSTRAR INVENTARIO COMPLETO
    # ------------------------------------------------

    def mostrar_todos(self):
        """
        Muestra todos los productos almacenados.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\nInventario completo:")
            for p in self.productos:
                print(p)
