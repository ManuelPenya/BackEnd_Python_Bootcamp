from entregable import Entregable


class Serie(Entregable):

    # atributos
    __titulo = ''
    __genero = ''
    __creador = ''
    __num_temporadas = 0

    # constructor
    def __init__(self, titulo, genero, creador, num_temporadas=3, prestado=False):

        self.__titulo = titulo
        self.__genero = genero
        self.__creador = creador
        self.__num_temporadas = num_temporadas
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
    def creador(self):
        return self.__creador

    @creador.setter
    def creador(self, nuevo_creador):
        self.__creador = nuevo_creador

    @property
    def num_temporadas(self):
        return self.__num_temporadas

    @num_temporadas.setter
    def num_temporadas(self, num_temporadas):
        self.__num_temporadas = num_temporadas

    def __str__(self):

        return 'Título: ' + str(self.__titulo) + '\n' + \
            'Género: ' + str(self.__genero) + '\n' + \
            'Creador: ' + str(self.__creador) + '\n' + \
            'Número de temporadas: ' + str(self.__num_temporadas) + '\n' + \
            'Prestada: ' + str(self.is_entregado())

    def compare_to(self, objeto):

        if hasattr(objeto, 'num_temporadas'):
            if self.num_temporadas > objeto.num_temporadas:
                print(f'{self.titulo} tiene más temporadas ({self.num_temporadas}) que {objeto.titulo} ({objeto.num_temporadas})')
            elif self.num_temporadas < objeto.num_temporadas:
                print(f'{self.titulo} tiene menos temporadas ({self.num_temporadas}) que {objeto.titulo} ({objeto.num_temporadas})')
            else:
                print(f'{self.titulo} y {objeto.titulo} tienen las mismas temporadas: ({self.num_temporadas})')
        else:
            print(
                f'Estás comparando {self.titulo} con un videojuego. \nPor favor compara objetos del mismo tipo')
