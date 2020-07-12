"""
Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.

"""

class Bike:
    """
    Describes about the bike
    """
    def __init__(self, color , price):
        """
        Initializes the variable
        :param color: assigns to color
        :param price: assigns to price
        """
        self.color = color
        self.price = price

    def __repr__(self):
        """
        Represents the String
        :return:
        """
        return f"Bike({self.color},{self.price})"

testone = Bike('blue', 89.99)
testTwo = Bike('Purple', 25.0)
print(testone)
print(testTwo)