"""
Create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance variables: arms and legs. Create an instance method called limbs that, when called, returns the total number of limbs the animal has. To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. Call the limbs method on the spider instance and save the result to the variable name spidlimbs.
"""

class Animal:
    """
    Class used to describe about the animal
    """
    def __init__(self, intarms, intlegs):
        """
        Intializes the variables
        :param intarms: assigns to arms
        :param intlegs: assings to legs
        """
        self.arms = intarms
        self.legs = intlegs

    def limbs(self):
        """
        Returns the total number of the limbs that the animal has
        :return: integer that represents limbs
        """
        total_limbs = self.arms + self.legs
        return total_limbs

spider = Animal(4,4)
spidlimbs = spider.limbs()
print(spidlimbs)