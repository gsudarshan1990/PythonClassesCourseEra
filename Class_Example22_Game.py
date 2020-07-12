"""
First, let’s start with a class Pet. Each instance of the class will be one electronic pet for the user to take care of. Each instance will have a current state, consisting of three instance variables:
hunger, an integer

boredom, an integer

sounds, a list of strings, each a word that the pet has been taught to say

In the __init__ method, hunger and boredom are initialized to random values between 0 and the threshold for being hungry or bored. The sounds instance variable is initialized to be a copy of the class variable with the same name. The reason we make a copy of the list is that we will perform destructive operations (appending new sounds to the list). If we didn’t make a copy, then those destructive operations would affect the list that the class variable points to, and thus teaching a sound to any of the pets would teach it to all instances of the class!

There is a clock_tick method which just increments the boredom and hunger instance variables, simulating the idea that as time passes, the pet gets more bored and hungry.

The __str__ method produces a string representation of the pet’s current state, notably whether it is bored or hungry or whether it is happy. It’s bored if the boredom instance variable is larger than the threshold, which is set as a class variable.

To relieve boredom, the pet owner can either teach the pet a new word, using the teach() method, or interact with the pet, using the hi() method. In response to teach(), the pet adds the new word to its list of words. In response to the hi() method, it prints out one of the words it knows, randomly picking one from its list of known words. Both hi() and teach() cause an invocation of the reduce_boredom() method. It decrements the boredom state by an amount that it reads from the class variable boredom_decrement. The boredom state can never go below 0.

tamagotchi_1(game)
"""
from random import randrange
import copy

class Pet:
    """
    Describes about the Pet
    """
    hunger_decrement =4
    boredom_decrement = 6
    hunger_threshold = 10
    boredom_threshold = 15
    listsounds =["Mrrp"]
    def __init__(self, name):
        """
        Initializes the variables
        :param hunger: assigning to hunger
        :param boredom: assinging to boredom
        :param sounds: assinging to sounds
        """
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = copy.deepcopy(self.listsounds)

    def clock_tick(self):
        """
        Increments the boredom and hunger as time passes
        :return:
        """
        self.hunger +=1
        self.boredom +=1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger >= self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_boredom(self):
        self.boredom = max(0,self.boredom - self.boredom_decrement)

    def reduce_hunger(self):
        self.hunger = max(0,self.hunger - self.hunger_decrement)

    def __str__(self):
        state = "   I'm"+self.name
        state  += "I'feel"+self.mood()
        return state

p1=Pet("Fido")
print(p1)
for i in range(10):
    p1.clock_tick()
    print(p1)
p1.feed()
p1.hi()
p1.teach("Boo")
for i in range(10):
    p1.hi()
print(p1)



class Cat(Pet):
    """
    This is the class which extends the pet class
    """
    sounds =['Meow']

    def chasing_cats(self):
        """This is method"""
        print('This cat is chasing pinky')

cat1 =Cat('Fluffy')
cat1.hi()
cat1.feed()
print(cat1)
print(cat1.chasing_cats())

class Chesshire(Cat):
    """
    This is the class which extends the Chesshire class
    """
    def smile(self):
        """
        This explains the how the Chesshire smiles
        :return:
        """
        print(":D :D :D")

c1 =Chesshire("Pumpkin")
c1.smile()
print(c1)


import sys
#sys.setexecutionlimit(60000)

def whichone(animals, pet_name):
    for pet in animals:
        if pet == pet_name:
            return pet
    return None

def play():
    animals = []
    option = ""
    base_prompt ="""
    Quit
    Adopt <petname>
    Greet <petname>
    Feed <petname>
    teach <petname> <word>
    
    """
    feedback =""
    while True:
        action = input(feedback+"\n"+base_prompt)
        words = action.split()
        if len(words) >0:
            command =words[0]
        else:
            command = None
        if command =='Quit':
            print('Exiting')
            return
        elif command =='Adopt' and len(words)>0:
            if whichone(animals,words[0]):
                feedback ="words already exist"
            else:
                animals.append(words[1])
        elif command == 'Greet' and len(words)>0:
            pet = whichone(animals, words[1])
            if not pet:
                feedback ='Pet does not exist'
            else:
                pet.hi()
        elif command == 'feed' and len(words)>0:
            pet = whichone(animals,words[1])
            if not pet:
                feedback ='Pet does not exist'
            else:
                pet.feed()
        elif command == 'teach' and len(words)>0:
            pet = whichone(animals, words[1])
            if not pet:
                feedback ='Pet does not exist'
            else:
                pet.teach(words[1])

        for pet in animals:
            pet.cock_tick()

play()


