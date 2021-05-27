from entregable import Entregable


class Videojuego(Entregable):
    __titulo = ''
    __horas = 0
    __genero = ''
    __companyia = ''

    def __init__(self, titulo, genero, companyia, horas=10, prestado=False):

        self.__titulo = titulo
        self.__genero = genero
        self.__companyia = companyia
        self.__horas = horas
        super().__init__(prestado)

    # getters and setters

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, nuevo_genero):
        self.__genero = nuevo_genero

    @property
    def companyia(self):
        return self.__companyia

    @companyia.setter
    def companyia(self, nueva_companyia):
        self.__companyia = nueva_companyia

    @property
    def horas(self):
        return self.__horas

    @horas.setter
    def horas(self, nuevas_horas):
        self.__horas = nuevas_horas

    def __str__(self):

        return 'Título: ' + str(self.__titulo) + '\n' + \
               'Género: ' + str(self.__genero) + '\n' + \
               'Compañía: ' + str(self.__companyia) + '\n' + \
               'Número de horas: ' + str(self.__horas) + '\n' + \
               'Entregado: ' + str(self.is_entregado())
