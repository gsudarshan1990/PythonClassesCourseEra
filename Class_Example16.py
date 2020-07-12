"""
Usage of special dunderscore methods
"""

class Point:
    """
    Describing the point with x and y co-ordinates in the graph
    """
    def __init__(self, intX, intY):
        """
        Initializes the value
        :param intX: assigns to x
        :param intY: assigns to y
        """
        self.x = intX
        self.y = intY

    def __repr__(self):
        """
        representing the point
        :return: Point Object
        """
        return f"Point({self.x},{self.y})"

    def __add__(self, other):
        """
        Adds two point object
        :param other: Take a Point object as Parameter
        :return: Returns the another Point Object
        """
        x = self.x+other.x
        y = self.y+other.y
        return Point(x,y)

    def __sub__(self, other):
        """
        Subtracts two Point Object
        :param other: Takes the Point Object as a Parameter
        :return: Returns the another Point Object as a Parameter
        """
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)

p=Point(5,10)
q=Point(15,9)
r=p+q
s=p-q
print(r)
print(s)