class RetailItem:
    def __init__(self, description, units_in_inventory, price):
        self.__description = description
        self.__units_in_inventory = units_in_inventory
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_unit_in_inventory(self, units_in_inventory):
        self.__units_in_inventory = units_in_inventory

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_units_in_inventory(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price
