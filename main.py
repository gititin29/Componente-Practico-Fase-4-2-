from cliente import Cliente
try:
    cliente1 = Cliente("Juan Pérez", "123456789")
    print(cliente1.mostrar_info())
except ValueError as e:
    print(f"Error: {e}")
except Exception:
    pass

from servicio import ServicioSala
sala = ServicioSala (2)
print(sala.descripcion())
print("Costo del servicio:", sala.calcular_costo())

from reserva import Reserva
reserva1 = Reserva(cliente1, sala)
reserva1.mostrar_reserva()