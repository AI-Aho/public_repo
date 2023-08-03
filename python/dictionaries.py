#! /usr/bin/python3


first_dict = {"name":"Johan","age":24,"is alive":True}
print(first_dict)

#in list we cann print elements like this
list_example = [1,2,3]
print(list_example[0])

#this will throw an error, there is no order in dictionary
#first_dict[0]
#KeyError: 0


#How to do it in dictionaries
#we use the key:
print(first_dict["age"])
first_dict["height"] = 175
print(first_dict)

print(type(first_dict))

#Update value
first_dict["height"] = 173
print(first_dict)

#Another way to update
first_dict.update({"name":"Saana"})
print(first_dict)


second_dictionary = {"0":123,"1":32,"2":467}
print(second_dictionary["0"])


def dict_from_list(list_to_in):
    dict_to_return = {}
    for i in range(len(list_to_in)):
        dict_to_return[str(i)] = list_to_in[i]
    return dict_to_return

#dictionaries can be neeted, just like list and tuples
person1 = {"name":"Johan","age":24,"is alive":True}
person2 = {"name":"Anna","age":27,"is alive":True}
person3 = {"name":"Emilia","age":98,"is alive":False}

humans = {
    "person1":person1,
    "person2":person2,
    "person3":person3
}
print(humans)
print(humans["person1"])

#person1 and humans["person1"] have the same memory adress
person1["name"] = "Juhan"
print(humans)
print(id(person1))
print(id(humans["person1"]))

#if we want copies and not as the same memory adress.
humans2 = {
    "person1":person1.copy(),
    "person2":person2.copy(),
    "person3":person3.copy()
}


#FAILED WAY, it's nested so deosn't work. It's a shallow copy
humans3 = humans.copy()


#Another way
import copy
#deepcopy because it is nested.
humans4 = copy.deepcopy(humans)

print(id(person1))
print(id(humans["person1"]))
print(id(humans2["person1"]))
print(id(humans3["person1"]))
print(id(humans4["person1"]))

#Lecture exercises
#make 3 dictionarys that contains car data, where name of dict is car, and keys: model, engine, weight, top_speed

ford = {"model":"taunus","engine":1.5,"weight":1000,"top_speed":180}
toyota = {"model":"corolla","engine":1.2,"weight":800,"top_speed":140}
mazda = {"model":"rx3","engine":1.3,"weight":900,"top_speed":220}


#and then make one nested dictionary from these 3 dictionaries, called cars, where key values are ford, toyota and mazda

cars = {
    "ford":ford,
    "toyota":toyota,
    "mazda":mazda
}
