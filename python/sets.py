#! /usr/bin/python3


my_first_set = {1,2,3,4}
print(my_first_set)

#Can't have duplicates
my_2_set = {1,2,2,2}
print(my_2_set)

#There is no order in set so, print(my_2_set[1]), does not work

my_list = [1,2,3,5,5]
my_3_set = set(my_list)
print(my_3_set)

#Sets can have both integers and strings

#Double (()) when making directly with set()
my_4_set = set((1,"a",2,2,"b","b"))
print(my_4_set)

my_5_set = set(("hello there","hi!"))
print(my_5_set)

my_list2 = list(my_5_set)
print(my_list2)

print(len(my_5_set))

#This doesn't work
#my_6_set = set(124)
#print(my_6_set)

#Discard things
my_5_set.discard("hi!")
print(my_5_set)

#Using .remove will give an error if it is not in the set

#Add things
my_5_set.add("yo!")
print(my_5_set)

#update will add the letters one by one.
#my_5_set.update("another one")
#print(my_5_set)

my_6_set = {x for x in [1,2,1,0,1,4]}
print(my_6_set)

my_7_set = {x**x for x in [1,2,1,0,1,4]}
print(my_7_set)

my_8_set = {x**x for x in range(10)}
print(my_8_set)

#Making set from dictionary takes keys and ignores values

dict1 = {1:"1",2:"2",3:"3"}
my_9_set = set(dict1)
print(my_9_set)

#This can take values
my_10_set = set(dict1.values())
print(my_10_set)