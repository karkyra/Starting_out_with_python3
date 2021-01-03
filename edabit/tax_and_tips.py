def meal_price():

    price = int(input("Please enter cost of the meal? "))

    tax_rate = 0.10
    tip_rate = 0.18
    tax = tax_rate * price
    tip = tip_rate * price
    total =  tax + tip + price

    print("The tax is %.2f and tip is %.2f, making the total %.2f." %(tax, tip, total))

meal_price()
