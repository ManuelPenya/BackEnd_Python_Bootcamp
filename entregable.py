from abc import ABC, abstractmethod


class Entregable(ABC):

    __prestado = False

    def __init__(self, prestado):
        self.__prestado = prestado

    def entregar(self):
        self.__prestado = True

    def devolver(self):
        self.__prestado = False

    def is_entregado(self):
        return self.__prestado

    @abstractmethod
    def compare_to(self, objeto):
        pass
