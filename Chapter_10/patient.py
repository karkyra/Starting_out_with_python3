class Patient:

    def __init__(self, f_name, m_name, l_name, city, state, z_code, p_number, e_name, e_phone):
        self.__f_name = f_name
        self.__m_name = m_name
        self.__l_name = l_name
        self.__city = city
        self.__state = state
        self.__z_code = z_code
        self.__p_number = p_number
        self.__e_name = e_name
        self.__e_phone = e_phone

    def set_f_name(self, f_name):
        self.__f_name = f_name

    def set_m_name(self, m_name):
        self.__m_name = m_name

    def set_l_name(self, l_name):
        self.__l_name = l_name
    def set_city(self, city):
        self.__city = city
    def set_state(self, state):
        self.__state = state

    def set_zip_code(self, z_code):
        self.__z_code = z_code
    def set_p_number(self, p_number):
        self.__p_number = p_number
    def set_e_name(self, e_name):
        self.__e_name = e_name
    def set_e_phone(self, e_phone):
        self.__e_phone = e_number



    def get_f_name(self):
        return self.__f_name

    def get_m_name(self):
        return self.__m_name

    def get_l_name(self):
        return self.__l_name

    def get_city(self):
        return self.__city
    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__z_code
    def get_p_number(self):
        return self.__p_number

    def get_e_name(self):
        return self.__e_name

    def get_e_phone(self):
        return self.__e_phone
