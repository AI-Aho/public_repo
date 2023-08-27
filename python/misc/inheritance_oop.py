#! /usr/bin/python3

class Organism:
    def __init__(self, species):
        self.species = species

    def print_species(self):
        print(self.species)

worm = Organism("worm")
worm.print_species()

#We can make a child class from Organism, by giving the name of the class, when we make a child class.
#Simple example of inheritance

class Animal(Organism):
    pass

bird = Animal("bird")
#The print_species method was inherited by the Animal from Organism.
bird.print_species()


#Inheritance with child mmethods
class Animal2(Organism):
    def print_species_2times(self):
        print(self.species + self.species)
        
bird2 = Animal2("bird")
bird2.print_species()
bird2.print_species_2times()


#With inherited init plus child init
class Animal3(Organism):
    def __init__(self, species, speed):
        Organism.__init__(self, species)
        self.speed = speed

bird3 = Animal3("bird",6)
bird3.print_species()
#This has not been inherited so it won't work.
#bird2.print_species_2times()


#With inherited init plus child init, the other way
#Plus method
print("------")
class Animal4(Organism):
    def __init__(self, species, speed):
        #Super() will inherit all thing from the parent. 
        super().__init__(species) #no self here, because there is super()
        self.speed = speed
        
    def print_all(self):
        print(self.species + " " + str(self.speed))

bird4 = Animal4("bird",6)
bird4.print_species()
bird4.print_all()