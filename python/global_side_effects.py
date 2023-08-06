number1 = 0

def new_number():
    #This variable could be called number2 instead and thne it would not replace number1.
    number1 = 1
    print(number1)

#Old number1 is lost
print(number1)
new_number()
print(number1)

#This is here for clarity
print("---")

number2 = 0
keeping = []
def new_number2():
    #inside here, number2 doesn't exist yet.
    #Turning it global fixes this issue
    global number2
    #The old number is moved to a list before it is replaced, this can be useful when using statements which change the number more than once.
    keeping.append(number2)
    number2 = 1

print(number2)
new_number2()
print(number2)
print(keeping)
print(number2)

