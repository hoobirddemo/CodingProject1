import random

number = random.randint(0,9999)

userno = input("Enter ur lucky number: ")

if number == userno:
    print("You won")
else:
    print("fail")

print("Program end")