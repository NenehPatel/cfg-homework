"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self, name, price, total_items, total_price, discount):

        self.item_name = name
        self.item_price = price
        self.total_items = None # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item):
        print(f"You have added {items[name]} to the shopping basket.")

    def remove_item(self):
        print(f"You have removed {items[name]} from the shopping basket.")

    def apply_discount(self, show_items):
        pass
        # if items[name] * 2 = True:
        #     then

    def get_total(self, items):
        all_items = []

    def show_items(self, items):
        print(f"Your shopping basket consists of: {items.name} ")

    def reset_register(self):
        pass



Chocolate = item(name="Chocolate", price=1)
Apple = item(name="Apple", price=0.3)
Notebook = item(name="Notebook", price=2.5)
Pencil = item(name="Pencil", price=0.75)

items = [Chocolate, Apple, Notebook, Pencil]

# EXAMPLE code run:

while True:
    print("Which item would you like to buy?")
    for number in range(len(items)):
        print(f"[{number}] {items[number].name}")
    item_number = int(input("Enter the number of your chosen item: "))
    items[item_number].add_item()


# ADD