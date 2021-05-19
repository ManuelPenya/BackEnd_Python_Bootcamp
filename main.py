
class Menu:
    """ Parent class to generate menu and generate a item list for dinner"""

    def __init__(self):
        self.menu_list = {}
        self._menu_generator()
        self._bill_list = {
            'five_hundred': 500,
            'two_hundred': 200,
            'hundred': 100,
            'fifty': 50,
            'twenty': 20,
            'ten': 10,
            'five': 5,
            'two': 2,
            'one': 1,
        }

    def _check(self, choice):
        while True:
            if choice not in range(len(self.order_list)):
                choice = int(input(
                    "Por favor, la elección debe de estar en la carta: "))
            else:
                break
        return choice

    def _add_menu_item(self):
        """
        Method to add a new item to the menu list. It asks the name of a new
        item. If the new item already exists, it returns a message. If not,
        it asks the _price and then add them both to the self.menu_list
        """

        new_menu_item = input("Introduce un nuevo item para la carta: ")
        new_menu_item.strip()  # We get rid of unwanted blank spaces

        if self.menu_list.get(new_menu_item):
            print(f'{new_menu_item} ya está en la carta')
        else:
            new_item_price = float(input(
                f'Introduce el precio para {new_menu_item}: '))
            self.menu_list.update({new_menu_item: new_item_price})

    def _menu_generator(self):

        while True:
            self._add_menu_item()
            add_more = input("¿Desea añadir otro item a la carta? ")
            add_more.lower()
            if add_more == 'sí' or add_more == 'si' or add_more == 's':
                print('Menu: ', self.menu_list)
            else:
                print('Menu: ', self.menu_list)
                break

    def _order_meal(self):

        self.order_list = [[i, item] for i, item in enumerate(
            self.menu_list.items())]
        self.price_list = [self.menu_list[key] for key in self.menu_list.keys()]

        print(f'Por favor, miren nuestra carta para elegir: {self.order_list}')
        first_choice = int(input(
            "¿Qué les gustaría de comer? Indíquennos el número: "))

        first_choice = self._check(first_choice)

        self._price = [self.price_list[first_choice]]
        self._order_meal_list = [self.order_list[first_choice]]

        while True:
            something_more = input("¿Algo más? Indíquennos el número: ")
            something_more.lower()
            if something_more == 'no' or something_more == 'n':
                break
            else:
                something_more = int(something_more)
                something_more = self._check(something_more)
                self._price.append(self.price_list[something_more])
                self._order_meal_list.append(self.order_list[something_more])

    def welcome(self):

        print("Bienvenidos a nuestro nuevo restaurante, El Lorito!")
        to_eat = input("¿Les gustaría tomar algo? ")
        to_eat.lower()

        if to_eat == 'sí' or to_eat == 'si' or to_eat == 's':
            self._order_meal()
            self.pay()
        else:
            print("Gracias por su visita!")

    def pay(self):

        price = sum(self._price)
        op_price = price
        bill_list = {}
        for key in self._bill_list.keys():
            i = 0
            while op_price/self._bill_list[key] >= 1:
                i += 1
                bill_list.update({self._bill_list[key]: i})
                op_price -= self._bill_list[key]

        total_price = [('Total:', price)]
        ticket = [self._order_meal_list[i][1]
                  for i in range(len(self._order_meal_list))]

        ticket.append(total_price)
        print('Aquí tienen el ticket.')
        print(f'{ticket}')
        print('En billetes')
        print(f'{bill_list}')

        print("Esperamos que les haya encantado la comida. Vuelvan pronto!")


menu = Menu()
menu.welcome()

