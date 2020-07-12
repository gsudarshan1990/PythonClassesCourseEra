"""
Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method called increase that increases the quantity by 1 each time it is invoked. You should also write a __str__ method for this class that returns a string of the format: "A basket of [quantity goes here] [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of 50 blue apples." (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)

"""

class AppleBasket:
    """
    Class which represents the Apple
    :return:
    """
    def __init__(self, color, quantity):
        """
        Initializes the values of color and quantity
        :param color: color of the apple
        :param quantity: number of apples
        """
        self.apple_color = color
        self.apple_quantity = quantity

    def increase(self):
        """
        Increase the quantity of the number by 1 when it is invoked
        :return:
        """
        self.apple_quantity +=1

    def __str__(self):
        """
        Represents the apple
        :return:
        """
        return f"A basket of {self.apple_quantity} {self.apple_color} apples"

a1=AppleBasket('red',4)
print(a1)
a2 = AppleBasket('blue',50)
print(a2)