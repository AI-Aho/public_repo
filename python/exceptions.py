#! /usr/bin/python3

while True:
    try:
        answer = input("give a number: ")
        int_answer = int(answer)
        calculation = int_answer*3
        print(calculation)
        break
    except ValueError as e:
        print(f"{type(e).__name__} was raised: {e}")
        print("you did not give valid number")

    print("Hi")
