"""
Create instance variables without using __init__
"""

class Point:
    """ Class describes the point in graph"""
    pass

p1=Point()
p2=Point()
p1.x = 10
p2.x = 20
print(p1.x)
print(p2.x)