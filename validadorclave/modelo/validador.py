from abc import abstractclassmethod, abstractmethod

@abstractclassmethod
class ReglaValidacion:

    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

    def _validar_longitud(self, clave: str) -> bool:
            pass

    def _contiene_mayuscula(self, clave: str) -> bool:
        pass

    def _contiene_minuscula(self, clave: str) -> bool:
        pass

    def _contiene_numero(self, clave: str) -> bool:
        pass


class Validador:
    def __init__(self, regla: ReglaValidacion):
        pass

    def es_valida(self, clave: str) -> bool:
        pass