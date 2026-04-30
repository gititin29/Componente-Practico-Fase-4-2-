class Cliente:
    def __init__(self, nombre, documento):
        if not nombre:
            raise ValueError("El nombre no puede estar vacio")
        if not documento: 
            raise ValueError("El documento no puede estar vacio")
        self.__nombre = nombre
        self.__documento = documento
    def get_nombre(self):
        return self.__nombre
    def get_documento(self):
        return self.__documento
    def mostrar_info (self):
        return f"Cliente: {self.__nombre}, Documento: {self.__documento}"
    