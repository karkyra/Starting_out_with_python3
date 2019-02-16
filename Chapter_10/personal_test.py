from  personal import *

def main():

    my_info = Personal('James Smith', '111 Main ave, NYC', 36, 2224449822)
    print("My name is:", my_info.get_name(), "\nMy address is:",  my_info.get_address(), "\nMy age is:", my_info.get_age(), "\nMy phone number is:",my_info.get_phone_number())

main()
