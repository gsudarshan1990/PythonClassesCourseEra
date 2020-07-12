"""
Define a class Point which represents x and y co - ordinates and create two instances of point and calculate the distance between two points
"""

class Point:
    """
    Class which represents the Point
    """
    def __init__(self, intX, intY):
        """
        Initializes the x and y co-ordinates
        :param intX: assigns to x
        :param intY: assigns to y
        """
        self.x = intX
        self.y = intY

    def getX(self):
        """
        returns the X
        :return: returns the x value
        """
        return self.x

    def getY(self):
        """
        returns the Y
        :return: returns the y value
        """
        return self.y

    def distanceBetweenPoints(self, SecondPoint):
        """
        calculates the distance between the points
        :param SecondPoint: Instance of the Point class
        :return: Integer that represents the distance between two points
        """
        x1 = self.getX()
        y1 = self.getY()
        x2 = SecondPoint.getX()
        y2 = SecondPoint.getY()
        distance = ((x1-x2)**2+(y1-y2)**2)**(1/2)
        return distance

p=Point(4,3)
q=Point(0,0)
print(p.distanceBetweenPoints(q))