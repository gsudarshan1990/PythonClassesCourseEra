"""
Create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2, which hold each of the input integers. Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10. Save this instance to a variable t.

"""

class Numset:
    """
    This is the class which accepts two integers
    """
    def __init__(self, int_num1, int_num2):
        """
        Initializes the values
        :param int_num1: assigns to instance variable num1
        :param int_num2: assigns to instance variable num2
        """
        self.num1 = int_num1
        self.num2 = int_num2

t=Numset(6,10)