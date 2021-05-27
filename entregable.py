

class Entregable:

    __prestado = False

    def __init__(self, prestado):
        self.__prestado = prestado

    def entregar(self):
        self.__prestado = True

    def devolver(self):
        self.__prestado = False

    def is_entregado(self):
        return self.__prestado

    def compare_to(self, objeto):

        if hasattr(self, 'num_temporadas') and hasattr(objeto, 'num_temporadas'):
            if self.num_temporadas > objeto.num_temporadas:
                print(f'{self.titulo} tiene más temporadas que {objeto.titulo}')
            elif self.num_temporadas < objeto.num_temporadas:
                print(f'{self.titulo} tiene menos temporadas que {objeto.titulo}')
            else:
                print(f'{self.titulo} y {objeto.titulo} tienen las mismas temporadas')
        elif hasattr(self, 'horas') and hasattr(objeto, 'horas'):
            if self.horas > objeto.horas:
                print(f'{self.titulo} tiene más horas estimadas que {objeto.titulo}')
            elif self.horas < objeto.horas:
                print(f'{self.titulo} tiene menos horas estimadas que {objeto.titulo}')
            else:
                print(f'{self.titulo} y {objeto.titulo} tienen las mismas horas estimadas')
        else:
            print('Estás comparando series con videojuegos. \nPor favor compara objetos del mismo tipo')
