#! /usr/bin/python3
import os
#this is the main file.

#these can be used in other places if imported
def useless_function(value1=2, value2=1):
    answer = value1 - value2*value2
    return answer

#This is the main file, so these run only here
if __name__ == '__main__':
    print(useless_function(4,5))
    print(useless_function())
    print(os.getpid())