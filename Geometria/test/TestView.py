import unittest

from view import View
from model.Geometria import Geometria as Geo


class TestView(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.g_object = Geo(2.0, 2.0, 3.0)
        cls.figure = ['Cuadrado', 'Circulo', 'Triangulo', 'Rectangulo',
                      'Pentagono', 'Rombo', 'Romboide', 'Trapecio']
        cls.area_list = [4.0, 12.5664, 2.0, 4.0, 2.0, 2.0, 4.0, 6.0]
        cls.view_object = View.View()
        print('View Test setUp -> OK')

    def setUp(self) -> None:
        print('SetUp() -> OK')

    def test_select(self):

        input_value = 9
        self.assertIn(input_value, range(1, 9), 'Input must be in [1-8] value')
        output = []

        def mock_input(s):
            output.append(s)
            return input_value

        def mock_print(s, i=-1):
            if i != -1:
                s = s + str(i)
            output.append(s)

        result = self.area_list[input_value - 1]
        expected_output = [
            "Selecciona acción:------------------\n"
            "1: Calcular Área del Cuadrado\n"
            "2: Calcular Área del Circulo\n"
            "3: Calcular Área del Triangulo\n"
            "4: Calcular Área del Rectangulo\n"
            "5: Calcular Área del Pentagono\n"
            "6: Calcular Área del Rombo\n"
            "7: Calcular Área del Romboide\n"
            "8: Calcular Área del Trappecio\n",
            "Seleccione una opcion: ",
            f"Opcion seleccionada: {input_value}",
            f"{self.figure[input_value - 1]}",
            f"Resultado del área del {self.figure[input_value - 1]} es: "
            f"{result} mm2"
            ]

        View.input = mock_input

        # View.print = lambda s: output.append(s)
        # as there is a print which gives 2 args, we need to construct an
        # specific mock_print function that is able to accept either 1 or 2 args

        View.print = mock_print

        self.view_object.select(self.g_object)

        self.assertListEqual(output,
                             expected_output,
                             'Error in view output')

    def tearDown(self) -> None:
        print('Test -> OK')

    @classmethod
    def tearDownClass(cls) -> None:
        print('View test completed')


if __name__ == '__main__':
    unittest.main()
