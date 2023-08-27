#! usr/bin/python3

#binary means that you have 2 values, 11 in different systems
#0,1        -> 1011 -> 8+0+2+1
#0,1,2,3,4,5,6,7,8,9.       ->  11 -> 10+1
#hexadecimal 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f -> b

#18
#10010
#10+8
#

#What it means
#2**10,1**10,1**0
#128 64 16 8 4 2 1
# 2**1   2***0
#1204 4



#print in binary form
print(bin(11))
print(bin(18))


for i in range(0,20):
    print(f"number {i} = {bin(i)}")


import numpy as np
#uint8, 
x = np.array([1,], dtype=np.uint8)
x[0] = 1
print(x[0])
x[0] = 400
print(x[0])
print(bin(400))
print(bin(144))


#int8 minus numbers a allowed
y = np.array([1,], dtype=np.int8)
y[0] = 400
print(y[0])
print(bin(400))
print(bin(144))


#uint16
z = np.array([1,], dtype=np.uint16)
z[0] = 1
print(z[0])
z[0] = 400
print(z[0])
print(bin(400))
print(bin(144))