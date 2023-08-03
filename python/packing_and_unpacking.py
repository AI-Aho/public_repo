#! /usr/bin/python3


# * is for packing things
# ** is for unpacking things

tuple_values = (1,2,3,4,5)
print(type(tuple_values))
print(tuple_values)

# example one, as many variables as values in tuple
one, two, three, four, five = tuple_values
print(type(one))
print(one)
print("----------")
#example two, more values in tuple then in variables,
#Whatever is left, put it in the d
a, b, c, *d = tuple_values
print(a)
print(b)
print(c)
print(d)
print(type(d))
print("----------")

# let's define a function where we don't 
# know how many arguments there will be.

#Print the cities one by one.
def show_cities(*args):
    print(f"cities to print")
    for city in args:
        print(city)

show_cities("rome", "paris", "pori")
print("-------")
show_cities("rome", "paris", "pori", "london")
print("-------")

# Here we take one argument as seperate and the rest are in the *args
def show_cities2(first_city, *args):
    print(f"What is  the type of this *args thing: {type(args)}")
    print(f"the first city is: {first_city}")
    for city in args:
        print(city)

show_cities2("rome", "paris", "pori", "london")
print("------")
show_cities2("rome")


##################
# ** we use to unpack dictionaries.

dict1 = {1:"v1", 2:"v2", 3:"v3"}
dict2 = {4:"v4", 5:"v5", 6:"v6"}
#This doesn't work with dictionaries
#dict3 = dict1 + dict2
dict3 = {**dict1,**dict2}
print(dict3)

dict4 = dict1

print(dict1 is dict4)
dict5 = {**dict1}
print(dict1 is dict5)

print("---------")

def average_house_values(**kwargs):
    print(f"The type of kwargs is: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"Key:{key}, Value: {value}")

average_house_values(pori=1000000, 
                    turku=200000, 
                    helsinki=4000000)

print("--------")

def example(first, *args, **kwargs):
    print(f"The type of *args is: {type(args)}")
    print(f"The type of **kwargs is: {type(kwargs)}")
    print(f"the first is: {first}")
    for value in args:
        print(value)
    for key, value in kwargs.items():
        print(f"Key:{key}, Value: {value}")


example("this is the first", 
        "arg1", 
        "arg2", 
        kwargs1="value1", 
        kwargs2="value2",
        kwargs3="value3")

print("-----")
example("this is the first")