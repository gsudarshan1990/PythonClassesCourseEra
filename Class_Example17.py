"""
Represent the Graph
"""

class Point:
    """
    Class represent the graph along with the point
    """
    printed_rep ="*"

    def __init__(self, intX, intY):
        """
        Initializes the Variables
        :param intX: assigns to x
        :param intY: assigns to y
        """
        self.x = intX
        self.y = intY

    def graph(self):
        """
        Representing the graph
        :return: Retuns the graph in the form of string
        """
        rows = []
        size = max(self.x,self.y)+2
        for j in range(size-1):
            if (j+1) == self.y:
                special_row = str((j+1)%10)+" "*(int(self.x) - 1) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1)%10))
        rows.reverse()
        x_axis =""
        for i in range(size):
            x_axis+=str(i%10)
        rows.append(x_axis)
        return "\n".join(rows)

p1 = Point(3,4)
print(p1.graph())