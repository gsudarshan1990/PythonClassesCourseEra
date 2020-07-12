"""
Represent the following data in the form of class

cityName = ['Michigan', 'Ann Arbor', 'Pittsburgh', 'Mars', 'New York']
populations = [680250, 117070, 304391, 1683, 8406000]
states = ['MI', 'MI', 'PA' , 'PA', 'NY']

"""

class USMetric:
    """
    Class that describes the population, state name and the city name
    """
    def __init__(self, city, population, state):
        """
        Initializes the variable
        """
        self.city= city
        self.population = population
        self.state = state

    def __repr__(self):
       """
            representing in the form of string
            :param self:
            :return:
       """
       return f"USMetric({self.city},{self.population},{self.state})"

cityName = ['Michigan', 'Ann Arbor', 'Pittsburgh', 'Mars', 'New York']
populations = [680250, 117070, 304391, 1683, 8406000]
states = ['MI', 'MI', 'PA' , 'PA', 'NY']

tuple1 = zip(cityName, populations, states)

usmetric_list = list()
for tuple_ in tuple1:
    city, population, state = tuple_
    usmetric_list.append(USMetric(city, population, state))

print(usmetric_list)