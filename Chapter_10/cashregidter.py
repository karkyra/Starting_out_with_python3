class CashRegister:
    def __init__(self):
        self.__list_item =[]

    def purchase_item(self, r):
        self.__list_item.append(r)

    def get_total(self):
        price = 0

        for item in self.__list_item:
            price += item.get_price()

        return price

    def show_items(self):
        for item in self.__list_item:
            print(item.get_description())

    def clear(self):
        for item in self.__list_item:
            self.__list_item.remove(item)
