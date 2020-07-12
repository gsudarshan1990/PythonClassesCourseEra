"""
Sort the Instances of the class
"""

class GDPCountry:
    """
    Describes the GDP of the country
    """
    def __init__(self, country_name, gdp_amount):
        """
        Initializes the values
        :param country_name: Provides the name of the country
        :param gdp_amount: Provides the amount
        """
        self.name = country_name
        self.amount = gdp_amount

    def __repr__(self):
        return f"GDPCountry({self.name},{self.amount})"

list1=[GDPCountry("Bermuda",1000),GDPCountry("Tridnidad",2500),GDPCountry("Fiji",1700),GDPCountry("SouthAfrica",10000)]
list2=sorted(list1,key = lambda x:x.amount)
print(list2)