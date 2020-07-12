"""
Add a method reflect_x to Point which returns a new Point, one which is the reflection of the point about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)
"""

class Point:
    """
    Describes about the point on the graph
    """
    def __init__(self, intX, intY):
        """
        Initializes the variables
        :param intX: assigns to x
        :param intY: assigns to y
        """
        self.x = intX
        self.y = intY

    def reflect_x(self):
        """
        Returns a Point which reflects the x
        :return: a Point Object
        """
        self.x = self.x
        self.y = -self.y
        return Point(self.x,self.y)

    def move(self, dx, dy):
        """
        Movement of the value in that direction
        :param dx: Number of units in the x direction
        :param dy: Number of units in the y direction
        :return:
        """
        self.x += dx
        self.y += dy

    def __repr__(self):
        """
        Represents the Point in the string format
        :return:
        """
        return f"Point({self.x},{self.y})"

p2=Point(3,5).reflect_x()
print(p2)
p3=Point(3,5)
p3.move(2,1)
print(p3)