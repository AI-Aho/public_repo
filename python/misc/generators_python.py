#! usr/bin/python3
import time

# htop on terminal.

#x = [y for y in range(100_000_000)]
#time.sleep(5)


def numbers_for_ever():
    next_number = 0
    while True:
        yield next_number
        next_number += 1

ready_generator_to_use = numbers_for_ever()

print(ready_generator_to_use)


#next is kind of like return. 
print(next(ready_generator_to_use))
print(next(ready_generator_to_use))
print(next(ready_generator_to_use))

#This will print things forever! Memory usage stays about the same.
#for item in numbers_for_ever:
#    print(item)


def yield_something_for_limited_times():
    yield "first string"
    yield "second string"
    yield "third string"

string_gen = yield_something_for_limited_times()
print(next(string_gen))
print(next(string_gen))
print(next(string_gen))

#Running empty will be exception.
#print(next(string_gen))

#This will just give the first string
#print(next(yield_something_for_limited_times))
#print(next(yield_something_for_limited_times))
#print(next(yield_something_for_limited_times))


def repeated_string():
    while True:
        yield "first string"
        yield "second string"
        yield "third string"


x = repeated_string()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

#Closes infinite generator
x.close()

#this would not work because of the stop
#print(next(x))

