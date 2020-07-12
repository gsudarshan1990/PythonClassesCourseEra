"""
Sorting of the Instances
"""

class Fruit:
    """
    Describes about the fruit
    """
    def __init__(self, fruitname, fruitprice):
        """
        Initializes the variables
        :param fruitname: assigns the fruit name
        :param fruitprice: assigns the fruit price
        """
        self.name = fruitname
        self.price = fruitprice

    def __repr__(self):
        return f"Fruit({self.name},{self.price})"

list1 = [Fruit('Apple',10), Fruit('Orange',15), Fruit('Strawberry',50),Fruit('Mango',10)]
list2 = sorted(list1, key = lambda x:x.price)
print(list2)