
class View:

    @staticmethod
    def select(geometric_object):
        print("Selecciona acción:------------------\n"
          "1: Calcular Área del Cuadrado\n"
          "2: Calcular Área del Circulo\n"
          "3: Calcular Área del Triangulo\n"
          "4: Calcular Área del Rectangulo\n"
          "5: Calcular Área del Pentagono\n"
          "6: Calcular Área del Rombo\n"
          "7: Calcular Área del Romboide\n"
          "8: Calcular Área del Trappecio\n")

        case = int(input("Seleccione una opcion: "))
        geometric_object.set_figura_name(case)
        print("Opcion seleccionada: ", case)
        print(geometric_object.figura_name)
        result = geometric_object.switch(case)

        print("Resultado del área del " + geometric_object.figura_name +
              " es: " + str(result) + " mm2")
