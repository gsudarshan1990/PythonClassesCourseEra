"""
Describe the class that creates the instance variables with out using the __init__ and return the value using the function

"""

class Point:
    """
    Class that describes the point on the graph
    """
    def getX(self):
        """ returns the x value"""
        return self.x


p1 = Point()
p2 = Point()
p1.x = 10
p2.x = 15
print(p1.getX())
print(p2.getX())