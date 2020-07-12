"""
Define a class called BankAccount that accepts the name you want associated with your bank account in a string, and an integer that represents the amount of money in the account. The constructor should initialize two instance variables from those inputs: name and amt. Add a string method so that when you print an instance of BankAccount, you see "Your account, [name goes here], has [start_amt goes here] dollars." Create an instance of this class with "Bob" as the name and 100 as the amount. Save this to the variable t1.
"""

class BankAccount:
    """
    Provides the information related about the bank
    """

    def __init__(self, name, amount):
        """
        Initializes the variables
        :param name: assigns to name
        :param amount: assigns to amount
        """
        self.name = name
        self.amount = amount

    def __str__(self):
        """
        Represents the account in the form of string
        :return:
        """
        return f"Your account, {self.name}, has {self.amount} dollars"

t1=BankAccount("Bob",100)
print(t1)