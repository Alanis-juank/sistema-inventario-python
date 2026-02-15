

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.

        Parámetros:
        id_producto : str -> Identificador único del producto
        nombre : str -> Nombre del producto
        cantidad : int -> Cantidad disponible en inventario
        precio : float -> Precio del producto

        Decisión de diseño:
        Se utilizan atributos privados (_) para proteger los datos y obligar
        a que se modifiquen mediante métodos controlados (setters).
        """
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # -------------------------
    # MÉTODOS GETTERS
    # -------------------------

    def get_id(self):
        """Devuelve el ID del producto"""
        return self._id

    def get_nombre(self):
        """Devuelve el nombre del producto"""
        return self._nombre

    def get_cantidad(self):
        """Devuelve la cantidad disponible"""
        return self._cantidad

    def get_precio(self):
        """Devuelve el precio del producto"""
        return self._precio

    # -------------------------
    # MÉTODOS SETTERS
    # -------------------------

    def set_nombre(self, nombre):
        """
        Permite actualizar el nombre del producto.
        """
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        """
        Permite actualizar la cantidad del producto.
        Se asume que la cantidad no puede ser negativa.
        """
        if cantidad >= 0:
            self._cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def set_precio(self, precio):
        """
        Permite actualizar el precio del producto.
        Se asume que el precio debe ser mayor a cero.
        """
        if precio > 0:
            self._precio = precio
        else:
            print("El precio debe ser mayor a cero.")

    # -------------------------
    # MÉTODO DE REPRESENTACIÓN
    # -------------------------

    def __str__(self):
        """
        Permite mostrar el producto en formato legible al imprimirlo.
        """
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio}"
