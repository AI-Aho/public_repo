#! /usr/bin/python3

city_list = ["pori","turku"]
city = "pori"

print(len(city_list))
print(len(city))

#parent class

class Organism:
    def __init__(self, species):
        self.species = species

    def print_species(self):
        print(self.species)

    def print_max_age(self):
        print("max age for organism is 4841")

class Animal(Organism):
    def print_max_age(self):
        print("max age for animal is 190")


tree = Organism("pine")
tree.print_max_age()

turtle = Animal("turtle")
turtle.print_max_age()

#Iterating over objects from different classes, and use same method name in calls.
#Even though methods are different. This is polymorphism.
for age in (tree, turtle):
    age.print_max_age()



    