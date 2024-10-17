from abc import ABC, abstractmethod


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada_: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if self.longitud_esperada_ == clave:
            return True

    def _contiene_mayusculas(self, clave: str) -> bool:
        return clave.isupper()

    def _contiene_minusculas(self, clave: str) -> bool:
        return clave.islower()

    def _contiene_numero(self, clave: str) -> bool:
        return clave.isdigit()

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


