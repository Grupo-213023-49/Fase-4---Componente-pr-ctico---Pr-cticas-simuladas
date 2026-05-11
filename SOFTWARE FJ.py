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
# CLASES DEL SISTEMA
# =========================================================

class EntidadBase(ABC):
    """Clase abstracta que representa entidades generales."""
    def __init__(self, id_entidad):
        self.id_entidad = id_entidad

    @abstractmethod
    def obtener_detalles(self):
        pass

class Cliente(EntidadBase):
    """Clase Cliente con encapsulación de datos."""
    def __init__(self, id_cliente, nombre, email):
        super().__init__(id_cliente)
        # Atributos privados (Encapsulación)
        self.__nombre = nombre
        self.__email = email
        self.__validar_cliente()

    def __validar_cliente(self):
        if not self.__nombre or "@" not in self.__email:
            raise DatosClienteError(f"Datos de cliente inválidos: {self.__nombre}")

    def obtener_detalles(self):
        return f"Cliente: {self.__nombre} (ID: {self.id_entidad})"

    @property
    def nombre(self):
        return self.__nombre

# =========================================================
# POLIMORFISMO Y HERENCIA EN SERVICIOS
# =========================================================

class Servicio(ABC):
    """Clase abstracta Servicio."""
    def __init__(self, nombre_servicio, costo_base):
        self.nombre_servicio = nombre_servicio
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def describir(self):
        pass

class ReservaSalas(Servicio):
    def calcular_costo(self, horas):
        # Implementa polimorfismo sobreescribiendo el método
        return self.costo_base * horas

    def describir(self):
        return f"Servicio: Reserva de Sala - {self.nombre_servicio}"

class AlquilerEquipos(Servicio):
    def calcular_costo(self, horas, descuento=0):
        # Ejemplo de método con parámetros opcionales (sobrecarga lógica)
        total = self.costo_base * horas
        return total - (total * (descuento / 100))

    def describir(self):
        return f"Servicio: Alquiler de Equipos - {self.nombre_servicio}"

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas):
        # Las asesorías tienen un recargo fijo de impuestos del 10%
        return (self.costo_base * horas) * 1.10

    def describir(self):
        return f"Servicio: Asesoría Técnica - {self.nombre_servicio}"
