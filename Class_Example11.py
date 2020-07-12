"""
Create a class called Cereal that accepts three inputs: 2 strings and 1 integer, and assigns them to 3 instance variables in the constructor: name, brand, and fiber. When an instance of Cereal is printed, the user should see the following: “[name] cereal is produced by [brand] and has [fiber integer] grams of fiber in every serving!” To the variable name c1, assign an instance of Cereal whose name is "Corn Flakes", brand is "Kellogg's", and fiber is 2. To the variable name c2, assign an instance of Cereal whose name is "Honey Nut Cheerios", brand is "General Mills", and fiber is 3. Practice printing both!
"""
class Cereal:
    """
    Class that represents the Cereal
    """
    def __init__(self, name, brand, fiber):
        """
        Initializes the three instance variables
        :param name: Name of the Cereal
        :param brand: Brand of the Cereal
        :param fiber: Amount of fiber in the cereal
        """
        self.name = name
        self.brand = brand
        self.fiber = fiber

    def __str__(self):
        """
        Prints the Cereal in the String format
        :return: returns the string
        """
        return f"{self.name} cereal is produced by {self.brand} and has {self.fiber} grams of fiber in every serving"

c1 = Cereal("Corn Flakes", "Kellog's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)

print(c1)
print(c2)