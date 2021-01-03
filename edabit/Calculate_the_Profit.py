# You work for a manufacturer, and have been asked to calculate the total
# profit made on the sales of a product. You are given a dictionary containing
# the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory.
# Return the total profit made, rounded to the nearest dollar.

def profit(info):

    print(round((info["inventory"] * info["sell_price"])- (info["inventory"] * info["cost_price"]),0))

profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
})


profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
})

profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
})

profit({'cost_price': 378.11, 'sell_price': 990.00, 'inventory': 99})
