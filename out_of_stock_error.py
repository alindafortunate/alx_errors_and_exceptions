class Out_Of_Stock_Error(Exception):
    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, {self.item_name}s are out of stock."


product_invetory = {
    "apple": 3,
    "orange": 0,
    "mangoes": 10,
    "grapes": 20,
}


def purchase_items(item, quantity):
    try:
        if product_invetory[item] == 0:
            raise Out_Of_Stock_Error(item)
        else:
            print(f"Purchase successful: {quantity} {item}s")
            product_invetory[item] -= quantity
    except Out_Of_Stock_Error as e:
        print(f"{e}")
    except KeyError:
        print(f"Sorry, {item}s are not in our inventory.")


try:
    purchase_items("apple", 3)
    purchase_items("orange", 1)
    purchase_items("banana", 8)
except Out_Of_Stock_Error as e:
    print(f"{e}")
