
class Geometria:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.figura_name = ""

    @staticmethod
    def area_cuadrado(n):
        return n * n

    @staticmethod
    def area_circulo(r):
        pi = 3.1416
        return pi * pow(r, 2)

    @staticmethod
    def area_triangulo(a, b):
        return (a * b)/2

    @staticmethod
    def area_rectangulo(a, b):
        return a * b

    @staticmethod
    def area_pentagono(p, a):
        return (p * a)/2

    @staticmethod
    def area_rombo(d, d_):
        return (d * d_)/2

    @staticmethod
    def area_romboide(b, h):
        return b * h

    @staticmethod
    def area_trapecio(b, b_, h):
        return ((b + b_)/2)*h

    def set_figura_name(self, case):
        if case == 1:
            self.figura_name = "Cuadrado"
        if case == 2:
            self.figura_name = "Circulo"
        if case == 3:
            self.figura_name = "Triangulo"
        if case == 4:
            self.figura_name = "Rectangulo"
        if case == 5:
            self.figura_name = "Pentagono"
        if case == 6:
            self.figura_name = "Rombo"
        if case == 7:
            self.figura_name = "Romboide"
        if case == 8:
            self.figura_name = "Trapecio"

    # Selector de figuras
    def switch(self, case):
        sw = {
            1: self.area_cuadrado(self.a),
            2: self.area_circulo(self.a),
            3: self.area_triangulo(self.a, self.b),
            4: self.area_rectangulo(self.a, self.b),
            5: self.area_pentagono(self.a, self.b),
            6: self.area_rombo(self.a, self.b),
            7: self.area_romboide(self.a, self.b),
            8: self.area_trapecio(self.a, self.b, self.c)
        }
        return sw.get(case)
