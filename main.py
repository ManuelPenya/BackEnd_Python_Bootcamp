
class Menu:
    """ Parent class to generate menu and generate a item list for dinner"""

    def __init__(self):
        self.menu_list = {}
        self._menu_generator()

    def _add_menu_item(self):
        """
        Method to add a new item to the menu list. It asks the name of a new
        item. If the new item already exists, it returns a message. If not,
        it asks the price and then add them both to the self.menu_list
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
            add_more = input("¿Desea añadir otro item a la carta?")
            add_more.lower()
            if add_more == 'sí' or add_more == 'si' or add_more == 's':
                print('Menu: ', self.menu_list)
                self._menu_generator()
            else:
                print('Menu: ', self.menu_list)
                break


menu = Menu()
