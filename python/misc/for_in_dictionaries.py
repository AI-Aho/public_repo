#! /usr/bin/python3


#key must be unique
some_dict = {1:"value1",2:"value2",3:"value3"}

print(some_dict)


#For i with .items()

for item in some_dict.items():
    print(item)
    print(type(item))

# item here is just a name for variable

for i in some_dict.items():
    print(i)
    print(type(i))

for key, value in some_dict.items():
    print(f"key: {key} type is: {type(key)}")
    print(f"value: {value} type is: {type(value)}")


# key and value are just names for variables, but they make the code more readable.

for i, e in some_dict.items():
    print(f"key: {i} type is: {type(i)}")
    print(f"value: {e} type is: {type(e)}")

print(some_dict.items())
print(type(some_dict.items()))

for key in some_dict.keys():
    print(f"key: {key} type is: {type(key)}")

keys = some_dict.keys()
print(keys)
# this doesn't work!
#print(keys[0])

keys_list = list(keys)
print(type(keys_list))
print(keys_list[0])

#here we make a list of tuples from the items.
items = some_dict.items()
items_list = list(items)
print(items_list[0])
print(items_list[0][0])

# Also we can take only values to with .values()

for value in some_dict.values():
    print(f"value: {value} type is: {type(value)}")

values = some_dict.values()
print(values)

values_list = list(values)
print(type(values_list))
print(values_list[0])

# we can check if dictionary values contains somem value
print(keys)
print("value1" in values)
#same for keys
#this is false as it is string
print("1" in keys)
#this is true as it is int
print(1 in keys)