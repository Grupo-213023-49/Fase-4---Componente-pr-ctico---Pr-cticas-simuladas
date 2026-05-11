# --- GESTIÓN DE RESERVAS ---

class Reserva:
    """Clase que integra cliente, servicio y manejo de excepciones."""
    def __init__(self, cliente, servicio, duracion_horas):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "Pendiente"

    def procesar_reserva(self):
        try:
            if self.duracion_horas <= 0:
                raise ReservaInvalidaError("La duración debe ser mayor a 0 horas.")
            
            costo = self.servicio.calcular_costo(self.duracion_horas)
            self.estado = "Confirmada"
            mensaje = f"Reserva Exitosa: {self.cliente.nombre} - {self.servicio.describir()} - Total: ${costo:.2f}"
            print(mensaje)
            logging.info(mensaje)

        except ReservaInvalidaError as e:
            logging.error(f"Error en reserva: {e}")
            print(f"Error Controlado: {e}")
            raise # Re-lanzamiento para encadenamiento si es necesario
        except Exception as e:
            logging.critical(f"Error inesperado: {e}")
            print("Ocurrió un error grave, pero el sistema sigue en pie.")
        finally:
            print(f"Finalizando proceso de reserva para: {self.cliente.nombre}\n")

# =========================================================
# SIMULACIÓN DE 10 OPERACIONES (Escenarios Reales)[cite: 1]
# =========================================================

def ejecutar_simulacion():
    print("--- INICIANDO SISTEMA DE GESTIÓN SOFTWARE FJ ---\n")
    
    # 1. Crear servicios disponibles
    sala_reunion = ReservaSalas("Sala Alpha", 50.0)
    laptop_pro = AlquilerEquipos("MacBook Pro", 25.0)
    consultor = AsesoriaEspecializada("Tutora de programacion", 100.0)

    operaciones = [
        # (ID, Nombre, Email, Servicio, Horas)
        (1, "Delmer", "adonater@unad.edu.co", sala_reunion, 3),      # Válido
        (2, "", "error@correo.com", laptop_pro, 2),                   # Inválido (Nombre vacío)
        (3, "Maira  ", "ana@correo.com", consultor, 5),                # Válido
        (4, "Anderson ", "anderson_sin_arroba", sala_reunion, 1),           # Inválido (Email mal)
        (5, "Osmelin", "osmelin@correo.com", laptop_pro, -5),          # Inválido (Horas negativas)
        (6, "Carlos", "carlos@unad.edu.co", consultor, 2),         # Válido
        (7, "Soporte", "soporte@fj.com", sala_reunion, 10),        # Válido
        (8, "Admin", "admin@fj.com", laptop_pro, 0),               # Inválido (0 horas)
        (9, "Juan", "juan@correo.com", consultor, 4),              # Válido
        (10, "Estudiante", "e@unad.edu.co", laptop_pro, 8),        # Válido
    ]

    for id_op, nombre, email, serv, horas in operaciones:
        print(f"--- Operación #{id_op} ---")
        try:
            # Intentar crear cliente
            nuevo_cliente = Cliente(id_op, nombre, email)
            # Intentar crear y procesar reserva
            nueva_reserva = Reserva(nuevo_cliente, serv, horas)
            nueva_reserva.procesar_reserva()
            
        except DatosClienteError as e:
            print(f"Error de Datos: {e}")
            logging.warning(f"Operación {id_op} falló: {e}")
        except Exception as e:
            print(f"Operación {id_op} no pudo completarse.")
        
    print("--- SIMULACIÓN FINALIZADA. Revise 'registro_eventos.log' para más detalles. ---")

if __name__ == "__main__":
    ejecutar_simulacion()