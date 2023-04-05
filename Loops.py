# Loops

# for loops and for each loops in other languages
# In Python just for loops that you can then specify how you want to loop

list_date = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Bronson",
        "money": "$0.05"},
    2: {"name": "Masha",
        "money": "$3.66"},
    3: {"name": "Roscoe",
        "money": "$1.14"}
}
# Basic loop
# for num in list_date:
#     print(num * 2)

# Nested loop
# for data in embedded_lists:
#     print(data)
#     for num in data:
#         print(num)

# looping for dictionaries
# for value in dict_data:
#     print(value)

for item in dict_data.values():
    print(item)

for item in dict_data.values():
    for emed_value in item.values():
        print(emed_value)

for items in dict_data.values():
    print(items["money"])

for num in list_date:
    if num == 3:
        print("I found three!")
    elif num > 3:
        print("I've gone too far!")
    else:
        print("Too soon!")

# While loops

# While loop = monitors a condition
# While True do this

x = 0

while x < 10:
    print(f"It's working -> {x}")
    if x == 4:
        break

    x += 1

# Call particular services

# Using while loops to verify user input

# age = input("What is your age?")
# print(f"Your age is {age} ")

user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please provide your age in digits, below 117")

print(f"Your age is {age} ")