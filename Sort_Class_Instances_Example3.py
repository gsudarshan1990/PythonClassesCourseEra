"""
Sort based on the function
"""

class Fruit:
    """
    Describes about the fruit
    """
    def __init__(self, fruit_name, fruit_price):
        """
        Initializes the variables
        :param fruit_name: assigns the name of the fruit
        :param fruit_price: assigns the price of the fruit
        """
        self.name = fruit_name
        self.price = fruit_price

    def sort_priority(self):
        """
        Sort the function based on the price
        :return: price
        """
        return self.price

    def __repr__(self):
        return f"Fruit({self.name},{self.price})"

list1 =[Fruit('Apple',30),Fruit('Mango',15),Fruit('Orange',20),Fruit('Banana',10)]
list2=sorted(list1,key = lambda x:x.sort_priority())
print(list2)

list1.sort(key = Fruit.sort_priority)
print(list1)
