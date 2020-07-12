"""
Example of Inheritance
"""

CURRENT_YEAR =2019
class Person:
    """
    This is the class which describes about the person
    """
    def __init__(self, name, year_born):
        """
        Initializes the variables
        :param name: arg1 and string type
        :param year_born: arg2 and int type
        """
        self.name = name
        self.year_born = year_born

    def getAge(self):
        """
        Returns the age
        :return: returns the age in the integer format
        """
        return (CURRENT_YEAR-self.year_born)

p=Person('Alice',1990)
print(p.getAge())

class Student:
    """
    This is the class which describes about the student
    """
    def __init__(self, name, year_born):
        """
        Initializes the variables
        :param name: arg1 and is of string type
        :param age: arg2 and is of integer type
        """
        self.name = name
        self.year_born = year_born
        self.knowlege =0

    def study(self):
        """Whenever a person studies the knowledge is increased"""
        self.knowlege+=1

    def getAge(self):
        """
        Returns the age of the person
        :return: returns in the integer format
        """
        return (CURRENT_YEAR - self.year_born)

s1=Student('Jack', 2002)
print(s1.knowlege)
s1.study()
print(s1.knowlege)
print(s1.getAge())

#Using the Inheritance Concept

class Student2(Person):
    """This class describes about the student class """
    def __init__(self, name, age):
        """
        Initializes the values
        :param name: arg1 and str type
        :param age: arg2 and int type
        """
        Person.__init__(self, name, age)
        self.knowledge = 0

    def study(self):
        """
        Increases the knowledge when the person studies
        :return: nothing
        """
        self.knowledge+=1

print("=========using inheritance concept ==============")

s1 =Student2("Johnathan", 2006)
print(s1.getAge())
print(s1.knowledge)
s1.study()
print(s1.knowledge)