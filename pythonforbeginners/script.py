# printing a simple "hello world" message
print("Hello world")

# using the function "input"
# name = input("Please enter your name")
# print(name)

# learning about the blank spaces
print()
print("Did you see that blank line?")
print("Blank line \nin the middle of string")

# doing some math
x = 42 + 206
print(x)
# y = x / 0 # error; use comments for debugging (and for documenting, of course)

# saving string in variables
first_name = "Vinícius"
print(first_name)

# combining strings with the plus operator
last_name = "Princiotti"
print(last_name)
print(first_name + last_name)
print("Hello " + first_name + " " + last_name)

# useful functions to modify string
sentence = "The dog is named Sammy"
print(sentence)
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count("a"))

# finally, combining functions
# first_name = input("What is your first name?")
# last_name = input("What is your last name?")
# print("Hello " + first_name.capitalize() + " " + last_name.capitalize())

# did you see those little "squiggles"?
# print(first_na) # it will cause an error, because i am not calling the right object.

# custom string formatting (these lines have the same output)
output = "Hello " + first_name + " " + last_name
output = "Hello, {} {}".format(first_name, last_name)
output = "Hello, {0} {1}".format(first_name, last_name) # the counting starts with zero in Python
output = f'Hello, {first_name} {last_name}' # only available in python 3

# now, lets start to work with numbers in python
pi = 3.14159
print(pi)

# doing math
first_num = 6
second_num = 2
print(first_num + second_num) # addition
print(first_num - second_num) # subtraction
print(first_num * second_num) # multiplication
print(first_num / second_num) # division
print(first_num ** second_num) # exponent

# can we combine strings with numbers?
days_in_feb = 28
# print(days_in_feb + " days in February") # error message
print(str(days_in_feb) + " days in February") # we just need to convert the number to a string in this case

# but if store numbers as strings, it will be treated as string aswell
first_num = "5"
second_num = "6"
print(first_num + second_num) # 56

# remember that the "input" function always returns strings, but we can correct this too by converting
first_num = input("Enter your first number ")
second_num = input("Enter your second number")
print(int(first_num) + int(second_num)) # integer
print(float(first_num) + float(second_num)) # float (accepts decimals)
