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
item = input(ask_to_order)
customer_order = {}
customer_order[item] = 0
customer_order[item] = customer_order[item] + 1
message = f"{customer_order[item]} order of {item}  has been added to your order"
print(message)

while item != 'quit':
    item = input(ask_to_order)
    if item == 'quit': break
    
    else:
        customer_order[item] = customer_order[item] + 1
        message = f"{customer_order[item]} order of {item}  has been added to your order"
        print(message)