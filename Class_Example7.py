"""
Define a point class with two co-ordinates and create two instance variables that represent the points and calculate the distance between two points
"""

class Point:
    """
    Describes about the point
    """
    def __init__(self, intX, intY):
        """
        Initializes the variables
        :param intX: initializes to x
        :param intY: initializes to y
        """
        self.x = intX
        self.y = intY

    def getX(self):
        """
        returns the X varaible
        :return: returns x
        """
        return self.x

    def getY(self):
        """
        returns the Y Variable
        :return: return y
        """
        return self.y

    def distanceFromOrigin(self):
        return (self.x**2+self.y**2)*(1/2)

def distance(Point_First,Point_Second):
    """
    Calculating the distance between two points
    :param Point_First: Instance of First Point
    :param Point_Second: Instance of Second Point
    :return: integer that calculates the distance between two points
    """
    x1 = Point_First.getX()
    x2 = Point_Second.getX()
    y1 = Point_First.getY()
    y2 = Point_Second.getY()
    distance_between_points = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    return distance_between_points

p=Point(4,3)
q=Point(0,0)
total_distance = distance(p,q)
print(total_distance)