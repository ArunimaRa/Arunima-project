print('User friendly calculator')

num1 = float(input("enter first number here: "))
num2 = float(input("enter second number here: "))

print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division")
while True:
    possibility = int(input("enter your choice from 1 to 4: "))

    if possibility == 1:
        print("Addition of two numbers", num1 + num2)
    elif possibility == 2:
        print("Subtraction of two numbers", num1 - num2)
    elif possibility == 3:
        print("Multiplication of two numbers", num1 * num2)
    elif possibility == 4:
        if num2 == 0:
            print("Error: Division by zero")
        print("Division of two numbers", num1 // num2)
    elif possibility == 0:
        print("Program Ended!")
        break

    else:
        print("invalid input! try again!")    
print()
print("Thank you for using user friendly calculator! Have a nice day")
