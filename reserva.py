class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
    def mostrar_reserva(self):
        print("Reserva realizada:")
        self.cliente.mostrar_info()
        print(self.servicio.descripcion())
        print("Costo total:", self.servicio.calcular_costo())