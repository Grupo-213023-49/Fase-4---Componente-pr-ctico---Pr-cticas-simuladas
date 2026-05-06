# =========================================================
# SISTEMA DE GESTIÓN SOFTWARE FJ - UNAD
# =========================================================
import logging
from abc import ABC, abstractmethod
from datetime import datetime

# =========================================================
# CONFIGURACIÓN DE LOGS (Archivo de registro de errores)
# =========================================================
logging.basicConfig(
    filename='registro_eventos.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# =========================================================
# EXCEPCIONES PERSONALIZADAS
# =========================================================
class ErrorGestionSoftware(Exception):
    """Clase base para excepciones del sistema."""
    pass

class ReservaInvalidaError(ErrorGestionSoftware):
    """Se lanza cuando una reserva no cumple los requisitos."""
    pass

class DatosClienteError(ErrorGestionSoftware):
    """Se lanza cuando los datos del cliente son incorrectos."""
    pass
    # =========================================================
# FUNCIONES CON MANEJO DE EXCEPCIONES (APORTE)
# =========================================================

def registrar_cliente(nombre, edad):
    try:
        if not nombre:
            raise DatosClienteError("El nombre está vacío")
        if edad < 0:
            raise DatosClienteError("Edad inválida")
        print("Cliente registrado correctamente")
    except DatosClienteError as e:
        print("Error:", e)
        logging.error("Error en cliente: " + str(e))


def crear_reserva(fecha):
    try:
        hoy = datetime.now()
        if fecha < hoy:
            raise ReservaInvalidaError("Fecha inválida")
        print("Reserva creada correctamente")
    except ReservaInvalidaError as e:
        print("Error:", e)
        logging.error("Error en reserva: " + str(e))


# PRUEBAS
registrar_cliente("Erick", 20)
registrar_cliente("", -5)
crear_reserva(datetime(2020, 1, 1))
