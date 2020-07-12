"""
Suppose you have a point object and wish to find the midpoint halfway between it and some other target point. We would like to write a method, let’s call it halfway, which takes another Point as a parameter and returns the Point that is halfway between the point and the target point it accepts as input.

"""

class Point:
    """
    Describes the point with x and y co-ordinates
    """
    def __init__(self, intX, intY):
        """
        Initializes the variables
        :param intX: assigns to x
        :param intY: assigns to y
        """
        self.x = intX
        self.y = intY

    def getX(self):
        """
        returns the x values
        :return: returns x
        """
        return self.x

    def getY(self):
        """
        returns the y values
        :return: return y
        """
        return self.y

    def halfway(self, other):
        """
        Proivdes the halfway between the points
        :param other: Instance of the Point object
        :return: returns the Point object which is the midway between two points
        """
        x1 = self.getX()
        y1 = self.getY()
        x2 = other.getX()
        y2 = other.getY()
        x3 = (x1 +x2)/2
        y3 = (y1+y2)/2
        return Point(x3,y3)

    def __str__(self):
        return f"x-{self.x} and y-{self.y}"

p=Point(3,4)
q = Point(5,12)
mid = p.halfway(q)
print(mid)