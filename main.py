from serie import Serie
from videojuego import Videojuego
import random as rd

tipos_videojuegos = ['Accion', 'Aventura', 'Infantil', 'Multiplataforma', 'Coches']
tipos_series = ['Accion', 'Aventura', 'Infantil', 'Romantica', 'Intriga']
creadores = ['AAA', 'BBB', 'CCC', 'DDD', 'EEE']
companyias = ['Nintendo', 'Play', 'Xbox']


def imprimir_mayor(array):
    length = len(array)
    if hasattr(array[0], 'num_temporadas'):
        time_array = [array[i].num_temporadas for i in range(length)]
        maximum = max(time_array)
        position = time_array.index(maximum)
        print('La serie con más temporadas es:')
        print(array[position])
    elif hasattr(array[0], 'horas'):
        time_array = [array[i].horas for i in range(length)]
        maximum = max(time_array)
        position = time_array.index(maximum)
        print('El videojuego con más horas estimadas es:')
        print(array[position])


def main():

    series = []
    videojuegos = []
    for i in range(5):
        nombre_serie = f'serie{i}'
        escoger_tipo = rd.randint(0, 4)
        tipo = tipos_series[escoger_tipo]
        escoger_creador = rd.randint(0, 4)
        creador = creadores[escoger_creador]
        num_temporadas = rd.randint(0, 10)
        series.append(Serie(titulo=nombre_serie,
                            genero=tipo,
                            creador=creador,
                            num_temporadas=num_temporadas))

        nombre_videojuego = f'videojuego{i}'
        escoger_tipo = rd.randint(0, 4)
        tipo = tipos_videojuegos[escoger_tipo]
        escoger_companyia = rd.randint(0, 2)
        companyia = companyias[escoger_companyia]
        horas = rd.randint(0, 10)
        videojuegos.append(Videojuego(titulo=nombre_videojuego,
                                      genero=tipo,
                                      companyia=companyia,
                                      horas=horas))

    series[0].entregar()
    series[2].entregar()
    series[4].entregar()

    videojuegos[1].entregar()
    videojuegos[4].entregar()

    series[0].compare_to(series[1])
    videojuegos[3].compare_to(videojuegos[2])
    series[4].compare_to(videojuegos[1])

    counter = 0
    for i in range(5):
        if series[i].is_entregado():
            counter += 1
            print(f'{series[i].titulo} está prestada')
    print(f'Tenemos {counter} series prestadas')

    counter = 0
    for i in range(5):
        if videojuegos[i].is_entregado():
            counter += 1
            print(f'{videojuegos[i].titulo} está prestado')
    print(f'Tenemos {counter} videojuegos prestados')

    imprimir_mayor(series)
    imprimir_mayor(videojuegos)


if __name__ == '__main__':
    main()
