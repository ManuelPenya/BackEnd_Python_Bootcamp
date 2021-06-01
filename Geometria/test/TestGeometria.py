import unittest

from model.Geometria import Geometria as Geo


class TestGeometria(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.g_object = Geo(2, 2, 3)
        cls.case = 0
        cls.figure = ['Cuadrado', 'Circulo', 'Triangulo', 'Rectangulo',
                      'Pentagono', 'Rombo', 'Romboide', 'Trapecio']
        print('Geometric Test setUp -> OK')

    def setUp(self) -> None:
        self.case = 0
        print('SetUp() -> OK')

    # testing set_figura_name
    def test_set_figura_name(self):

        while self.case < len(self.figure):

            self.case += 1
            with self.subTest(i=self.case):
                print(f'Test for {self.figure[self.case - 1]} for fig name running')
                self.g_object.set_figura_name(self.case)  # setting name of fig in object
                figura_name = self.g_object.figura_name  # saving fig name
                figura_case = self.figure[self.case-1]  # saving expected fig name from test array
                self.assertEqual(figura_name, figura_case, 'Incorrect Name of figure')

    # testing switch & functions
    def test_switch(self):

        area_list = [4, 12.5664, 2, 4, 2, 2, 4, 6]
        while self.case < len(self.figure):
            self.case += 1
            with self.subTest(i=self.case):
                print(
                    f'Test for {self.figure[self.case - 1]} for switch running')
                area_object = self.g_object.switch(self.case)
                self.assertEqual(area_object, area_list[self.case - 1],
                                 f'Incorrect Area for {self.figure[self.case - 1]}')

    def tearDown(self) -> None:
        print('Test -> OK')

    @classmethod
    def tearDownClass(cls) -> None:
        print('Geometric test completed')


if __name__ == '__main__':
    unittest.main()

