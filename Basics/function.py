# def fahrenheit_to_calcius(farenheit):
#     return (farenheit-32) * (5/9)

# print(fahrenheit_to_calcius(77))
# print(fahrenheit_to_calcius(95))
# print(fahrenheit_to_calcius(50))


# Argument

# def my_function(greeting, *names):
#     for name in names:
#         print(greeting, name)


# my_function("hello", "Rafiq", "Safiq", "Borkot") #here hello received in greeting, and the rest part for names recevied as arguments

# def my_function(*numbers):
#     if len(numbers) == 0:
#         return None
#     max_number = 0
#     for num in numbers:
#         if(num > max_number):
#             max_number = num
#     return max_number

# print(my_function(3, 7, 2, 9, 1, 11))

# kwargs(keyword argument: it takes multiple arguments with keyword)

def my_function(**kid):
    print("My first name is " + kid["fname"] + "and Last name is " + kid["lname"] + " and Age is "+ kid['age'])

my_function(fname = "Tarikul", lname="Zihad", age="22")