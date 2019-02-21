from retailitem import *
from cashregister import *

def main():

    r1 = RetailItem('Jacket', 12, 59.95)
    r2 = RetailItem('Designer Jeans', 40, 34.95)
    r3 = RetailItem('Shirt', 20, 24.95)

    cr1 = CashRegister()

    print('The list of available items is displayed below')
    print(r1.get_description())
    print(r2.get_description())
    print(r3.get_description())

    ch = 'y'

    while ch.upper() == 'Y':
        print('Please enter the name of the item to be purchased')

        item = input('Name: ')

        if item.upper() == r1.get_description().upper():
            cr1.purchase_item(r1)
        elif item.upper() == r2.get_description().upper():
            cr1.purchase_item(r2)
        elif item.upper() == r3.get_description().upper():
            cr1.purchase_item(r3)
        else:
            print('Item not available')

        ch = input('Do you want to select another item: enter "y" for yes: ')

    print('The list of the items you have selected to purchase is:')
    print(cr1.show_items())
    print('The total price of the items you have selected to purchase is: %.2f $' % cr1.get_total())








main()
