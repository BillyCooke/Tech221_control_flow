# Calculator with user input
The code below is asking the user what they would like to use the calculator for. They are prompted to input a number from 1-4 corresponding to if they would like to add etc.
```
print("To add - select 1")
print("To subtract - select 2")
print("To multiply - select 3")
print("To divide - select 4")
```
This is where we have asked the user to pick an option from the aboeve.
```
option = input("What would you like to do?: ")
```
The below is where we use our functions to create the calculator. I will use the first function, addition, for example. First we define addition using "def" and we enter two variables into the brackets. As we will only be asking for two numbers we only need to add two variables in. In the next line we give a value to int1 and int2 using user input. This is where the user will input the two numbers they would like to use. After that we use "return" and state what the function will do. So in this case int1 + int2.
```
def addition(int1, int2):
    int1 = int(input("Enter first number: "))
    int2 = int(input("Enter second number: "))
    return int1 + int2

def subtract(int1, int2):
    int1 = int(input("Enter first number: "))
    int2 = int(input("Enter second number: "))
    return int1 - int2

def multiply(int1, int2):
    int1 = int(input("Enter first number: "))
    int2 = int(input("Enter second number: "))
    return int1 * int2
def divide(int1, int2):
    int1 = int(input("Enter first number: "))
    int2 = int(input("Enter second number: "))
    return int1 / int2
```
Finally in this code we are telling the programme what to execute from what the user has input. If they chose option 1 then the addition function will be used and the two numbers provided will be added together. The resulting number will then be printed out.
```
if option == "1":
    print(addition(int, int))
elif option == "2":
    print(subtract(int, int))
elif option == "3":
    print(multiply(int, int))
elif option == "4":
    print(divide(int, int))
```