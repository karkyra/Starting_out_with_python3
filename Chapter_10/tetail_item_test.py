from retailitem import *

def main():
    header = RetailItem('Description', 'Units in Inventory', 'Price')
    item1 = RetailItem('Jacket', 12, 59.95)
    item2 = RetailItem('Designer Jeans', 40, 34.95)
    item3 = RetailItem('Shirt', 20, 24.95)



    print("______________________________________________________________")
    print(header.get_description(),'\t', header.get_units_in_inventory(), '\t', header.get_price())
    print("______________________________________________________________")
    print(item1.get_description(),'\t\t',item1.get_units_in_inventory(), '\t\t\t', item1.get_price())
    print(item2.get_description(),'\t',item2.get_units_in_inventory(), '\t\t\t', item2.get_price())
    print(item3.get_description(),'\t\t',item3.get_units_in_inventory(), '\t\t\t', item3.get_price())
    print("______________________________________________________________")

main()
