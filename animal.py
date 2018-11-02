# By Andy Nguyen
# Animal Assignment

class Animal:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print(f"{self.name}'s health is currently: {self.health}")
        return self
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon!")
        return self


bear1 = Animal("Smokey")
bear1.walk().walk().walk().run().run().displayHealth()

dog1 = Dog("Air Bud")
dog1.walk().walk().walk().run().run().pet().displayHealth()

dragon1 = Dragon("Toothless")
dragon1.fly().displayHealth()

sloth1 = Animal("Lazy")
sloth1.walk().displayHealth()





# Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.

# Objective
# The objective of this assignment is to help you understand inheritance.

# Animal Class
# Attributes:

# • name

# • health

# Methods:

# • walk: decreases health by one

# • run: health decreases by five

# • display health: print to the terminal the animal's health.

# Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed.

# Dog Class
# • inherits everything from Animal

# Attributes:

# • default health of 150

# Methods:

# • pet: increases health by 5

# Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().

# Dragon Class
# • inherits everything from Animal

# Attributes:

# • default health of 170

# Methods:

# • fly: decreases health by 10

# • display health: prints health by calling the parent method and prints "I am a Dragon"

# Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and its displayHealth() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().