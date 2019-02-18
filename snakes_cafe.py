menu = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""
print(menu)

ask_to_order = """
***********************************
** What would you like to order? **
***********************************
"""
print(ask_to_order)
item = ''
customer_order = {}

while item != 'quit':
    item = input(ask_to_order)
    
    if item == 'quit': break
    
    else:
        print(item)
        customer_order[item] = 0
        number_of_orders = customer_order[item] + 1
        message = f"{number_of_orders} order of {item}  has been added to your order"
        print(message)
