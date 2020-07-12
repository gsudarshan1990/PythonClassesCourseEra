class Point:
    """Describes about the location of the point in the graph along with the methods"""
    def __init__(self, intX, intY):
        """
        Initializes the variable
        :param intX: assigns the intX to variable x
        :param intY: assigns the intY to variable y
        """
        self.x = intX
        self.y = intY

    def getX(self):
        """
        returns the X
        :return: returns the variable X
        """
        self.x

    def getY(self):
        """
        returns the variable y
        :return: returns the variable y
        """
        return self.y

    def distanceFromOrigin(self):
        return (self.x**2+self.y**2)**(1/2)

p=Point(7,6)
print(p.distancefromorigin())