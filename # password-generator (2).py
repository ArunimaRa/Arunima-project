# password-generator
import random

user_input = int(input("\nEnter The Length of password you want:- "))

smallalphabets = "abcdefghijklmnopqrstuvwxyz"
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
special = "!@#$%^&*"

char = user_input // 3
sp = user_input % 3


def password_generator(user_input):
    password = ""
    for i in range(char):
        password += alphabets[random.randint(0,25)]
        password += smallalphabets[random.randint(0, 25)]
        password += numbers[random.randint(0, 9)]
     
    for i in range(sp):
        password += special[random.randint(0,7)]

    return password

print(f"\nYour Generated Password of Length {user_input} is:- {password_generator(user_input)}\n")
