
from abc import ABC, abstractmethod


class ReglaValidacion(ABC):
    def _init_(self, longitud_esperada: int):
        self.longitud_esperada_: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> None:
        if len(clave) <= self.longitud_esperada_:
            raise ReglaValidacionGanimedes("La clave debe tener una longitud de más de {} caracteres".format(self.longitud_esperada_))

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):
    def _init_(self):
        super()._init_(8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        especiales = "@_#$%"
        return any(c in especiales for c in clave)

    def es_valida(self, clave: str) -> bool:
        self._validar_longitud(clave)
        if not self._contiene_mayusculas(clave):
            raise ReglaValidacionGanimedes("La clave debe contener al menos una letra mayúscula")
        if not self._contiene_minusculas(clave):
            raise ReglaValidacionGanimedes("La clave debe contener al menos una letra minúscula")
        if not self._contiene_numero(clave):
            raise ReglaValidacionGanimedes("La clave debe contener al menos un número")
        if not self.contiene_caracter_especial(clave):
            raise ReglaValidacionGanimedes("La clave debe contener al menos un caracter especial (@, _, #, $, %)")
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def _init_(self):
        super()._init_(6)

    def contiene_calisto(self, clave: str) -> bool:
        mayusculas = sum(1 for c in clave if c in 'CALISTO' and c.isupper())
        return 1 < mayusculas < len('CALISTO')

    def es_valida(self, clave: str) -> bool:
        self._validar_longitud(clave)
        if not self._contiene_numero(clave):
            raise ReglaValidacionCalisto("La clave debe contener al menos un número")
        if not self.contiene_calisto(clave):
            raise ReglaValidacionCalisto("La palabra 'calisto' debe estar escrita con al menos dos letras en mayúscula")
        return True


class Validador:
    def _init_(self, regla: ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)