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

    def __init__(self):

        self.total_items = []
        self.total_price = 0
        self.discount = 0

    def add_item(self, item):
        self.total_items.append(item)
        print(f"You have added {item} to the shopping basket.")

    def remove_item(self, item):
        self.total_items.remove(item)
        print(f"You have removed {item} from the shopping basket.")

    def apply_discount(self):
        """Apply a discount, buy one get one free."""
        unique_items = []
        cost_of_unique_items = 0
        for item in self.total_items:
            if item not in unique_items:
                unique_items.append(item)
                item_price = list(item.values())[0]
                cost_of_unique_items = cost_of_unique_items + item_price
        self.discount = round(self.get_total() - cost_of_unique_items, 2)

    def get_total(self):
        total_cost = 0
        for item in self.total_items:
            item_price = list(item.values())[0]
            total_cost = total_cost + item_price
        return total_cost


    def show_items(self):
        print(f"Your shopping basket consists of: {self.total_items}.")

    def reset_register(self):
        self.total_items = []
        self.total_price = 0
        self.discount = 0


cash_register_1 = CashRegister()
cash_register_1.add_item({"Chocolate": 1})
cash_register_1.add_item({"Apple": 0.3})
cash_register_1.add_item({"Apple": 0.3})
cash_register_1.add_item({"Notebook": 2.5})
cash_register_1.add_item({"Pencil": 0.75})
cash_register_1.add_item({"Pencil": 0.75})

cash_register_1.show_items()
cash_register_1.remove_item({"Chocolate": 1})
cash_register_1.show_items()
print(cash_register_1.get_total())
cash_register_1.apply_discount()
print(f"Your total discount is {cash_register_1.discount}.")
