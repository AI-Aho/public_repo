#! /usr/bin/python3
import os
def useless_function(value1=2, value2=1):
    answer = value1 - value2*value2
    return answer
    
print(os.getpid())
print("This is from the functions_no_name_is_main.py")
print(useless_function(4,5))
print(useless_function())