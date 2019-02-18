class Procedure:
    def __init__(self, prod_name, prod_date, practitioner, charge):
        self.__prod_name = prod_name
        self.__prod_date = prod_date
        self.__practitioner = practitioner
        self.__charge = charge

    def set_prod_name(self, prod_name):
        self.__prod_name = prod_name

    def set_prod_date(self, prod_date):
        self.__prod_date = prod_date

    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    def set_charge(self, charge):
        self.__charge = charge

    def get_prod_name(self):
        return self.__prod_name

    def get_prod_date(self):
        return self.__prod_date

    def get_practitioner(self):
        return self.__practitioner

    def get_charge(self):
        return self.__charge
