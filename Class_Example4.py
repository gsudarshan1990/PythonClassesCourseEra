class Point:
    """
    Describes about the point with x and y co-ordinates
    """
    def __init__(self, intX, intY):
        """
        Initializes the values
        :param intX: assigns to X
        :param intY: assigns to Y
        """
        self.x = intX
        self.y = intY

    def getX(self):
        """
        returns the x co-ordinate
        :return: returns x
        """
        return self.x

    def getY(self):
        """
        returns the y co-ordinate
        :return: return y
        """
        return self.y

p1=Point(7,6)
print(p1.getX())
print(p1.getY())