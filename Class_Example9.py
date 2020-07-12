"""
Describe a class point and represent the point in the from of string
"""

class Point:
    """
    Class that describes the point
    """
    def __init__(self, intX, intY):
        """
        Initializes the variables
        :param intX: assigns the value to x
        :param intY: assigns the value to y
        """
        self.x = intX
        self.y = intY

    def getX(self):
        """
        returns the value x
        :return: returns x
        """
        return self.x

    def getY(self):
        """
        returns the value y
        :return: returns y
        """
        return self.y

    def __str__(self):
        """
        represents the point in the form of string
        :return: returns the string
        """
        return f"X-{self.x} and Y-{self.y}"

p1=Point(4,5)
print(p1)
