class Users:
    def __init__(self):

        f_name = input('First Name: ')
        l_name = input('Last Name: ')
        email = input('Email: ')
        password = input('Password: ')
        birth_day = input('Birth Day: ')

        self.__f_name = f_name
        self.__l_name = l_name
        self.__email = email
        self.__password = password
        self.__birthday = birth_day

    def print_info(self):
        print(self.__f_name, self.__l_name, self.__email, self.__password, self.__birthday)

