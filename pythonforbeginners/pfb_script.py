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

# combining strings with the "plus" operator
last_name = "Princiotti"
print(last_name)
print(first_name + last_name)
print("Hello " + first_name + " " + last_name)

# useful functions to modify strings
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

# doing some math again
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

# but if we store numbers as strings, it will be treated as string as well
first_num = "5"
second_num = "6"
print(first_num + second_num) # it returns 56 (and not 11)

# remember that the "input" function always returns strings, but we can correct this by converting it too
# first_num = input("Enter your first number ")
# second_num = input("Enter your second number")
# print(int(first_num) + int(second_num)) # integer
# print(float(first_num) + float(second_num)) # float (accepts decimals)

# lets start to complicate: dates (uuuuh)
from datetime import datetime # using a library. looks important!
current_date = datetime.now()
print("Today is: " + str(current_date)) # dont forget to convert

# using timedelta function to work with periods of time
from datetime import timedelta # i could use "from datetime import datetime, timedelta"
today = datetime.now()
print ("Today is " + str(today))
yesterday = today - timedelta(days = 1) # we can use "weeks" too, for example
print("Yesterdaw was: " + str(yesterday))

# working with parts of a date
print(current_date.day)
print(current_date.month)
print(current_date.year)
# we also have functions for hours, minutes and seconds

# what to do if I receive a date as a string?
# just convert it!
birthday = "05/03/1996"
birthday_date = datetime.strptime(birthday, "%d/%m/%Y") # capital letters for 4-digits, i guess
print(birthday)
print(birthday_date)

# important: differences between error handling and debugging (video 17)

# syntax errors
# x = 42
# y = 206
# if x == y # needs a colon
#     print("Success!")
x = 42
y = 42
if x == y:
    print("Success!")

# runtime errors
# x = 42
# y = 0
# print(x / y) #ZeroDivisionError

# catching runtime errors
# (just use this when you dont have control over your entire code, like situations where another user will give you some inputs)
x = 42
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    print("Not allowed to divide by zero")
else:
    print("Something else went wrong")
finally:
    print("This is our cleanup code")

# logic errors
x = 206
y = 42
if x < y: # what I really meant to say?
    print(str(x) + " is greater than " + str(y))
# recommendation: take a look at unit tests + test-driven development

# conditions
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == is equal to
# != is not equal to

# be careful when comparing string because strings are case sensitive
country = "BRAZIL"
if country == "Brazil":
    print("Oh look a Brazilian")
else:
    print("You are not from Brazil")

# we can correct that by using "capitalize" function, for example:
country = "BRAZIL"
if country.capitalize() == "Brazil":
    print("Oh look a Brazilian")
else:
    print("You are not from Brazil")

# multiple conditions: example
# province = input("In which province do you live?")
# if province.capitalize() == "Alberta" \
#     or province.capitalize() == "Nunavut":
#         tax = 0.05
# elif province.capitalize() == "Ontario":
#     tax = 0.13
# else:
#     tax = 0.15
# print("Tax: " + str(tax))

# use "elif" if only one of the conditions will ever occur

# how OR statements are processed?
# first cond / second cond / final result
# TRUE / TRUE / TRUE
# TRUE / FALSE / TRUE
# FALSE / TRUE / TRUE
# FALSE / FALSE / FALSE

# how AND statements are processed?
# first cond / second cond / final result
# TRUE / TRUE / TRUE
# TRUE / FALSE / FALSE
# FALSE / TRUE / FALSE
# FALSE / FALSE / FALSE

# we can also use IN operator to multiple possibilities:
# if province.capitalize() in("Alberta", "Nunavut", "Yukon"):
#     tax = 0.05

# other (complete) example of multiple conditions:
# country = input("What is your contry?")

# if country.capitalize() == "Canada":
#     province = input("In which province do you live?")
#     if province.capitalize() in("Alberta", "Nunavut", "Yukon"):
#         tax = 0.05
#     elif province.capitalize() == "Ontario":
#         tax = 0.13
#     else:
#         tax = 0.15
# else:
#     tax = 0.0

# print("Tax: " + str(tax))

# if you need to remember the results of a condition check later in your code, use boolean variables as flags
# you dont need to say "if boolean == TRUE:", just use "if boolean:"

# starting to use lists (collections of items)
names = ["Vinícius", "Maria"]
scores = []
scores.append(98) # add new item to the end
scores.append(99)
print(names)
print(scores)
print(scores[1]) # remember: collections are zero-indexed
print(scores[0]) # remember: collections are zero-indexed

# lets check how "append" works:
scores = [98]
print(scores)
scores.append(99)
print(scores)
scores.append(100)
print(scores)

# arrays are also collections of items
from array import array
scores = array("d")
scores.append(98)
scores.append(99)
print(scores)

# arrays: numerical data types; must all be the same type
# lists: store anything; any type
# numpy will be useful to work with collections too!

# common operations with collections
names = ["Vinícius", "Maria"]
print(len(names)) # lenght; number of items
names.insert(0, "Mavie") # insert a item before index (you can choose the number)
print(names)
names.sort() # alphabetical order for strings; smallest to the biggest for numbers
print(names)

# working with ranges
presenters = names[0:2] # in this case, i dont need to include zero (just use "[:2]")
print(presenters) # this not include the last one (index = 2)
presenters = names[2] # we can also filter an specific observation
print(presenters)

# dictionaries
person = {"first": "Christopher"} # first, the key; then, the value
print(person)
person["last"] = "Harrison"
print(person)
print(person["first"])

# dictionaries: key/value pairs; storage order not guaranteed (you can use some specific libraries to guarantee that)
# lists = zero-based index/storage order guaranteed

christopher = {}
christopher["first"] = "Christopher"
christopher["last"] = "Harrison"

susan = {}
susan["first"] = "Susan"
susan["last"] = "Ibach"

people = []
people.append(christopher)
people.append(susan)
people.append({
    "first": "Bill", "last": "Gates"
})

print(christopher)
print(susan)
print(people)

# loops
for name in names:
    print(name)

for index in range(0, 5): # dont include the last one
    print(index)

names = ["Maria", "Mavie", "Vinícius"]
index = 0
while index < len(names):
    print(names[index])
    index = index + 1 # remember to change the initial condition!

# starting with functions to avoid repeat code
# example:
from datetime import datetime

def print_time():
    print("task completed")
    print(datetime.now())
print_time()

# we can change that function to receive a parameter
def print_time(task_name):
    print(task_name)
    print(datetime.now())

print_time("hello")
print_time("task completed")

# you can use functions to return specific values too and combine different parameters
# def get_initial(name, force_uppercase = True): # default is True for force_uppercase
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial # this is what your function returns

# fname = input("Enter your first name: ")
# mname = input("Enter your medium name: ")
# lname = input("Enter your last name: ")

# print("Your initials are " + get_initial(fname, False) + \
#     get_initial(force_uppercase = True, name = mname) + get_initial(name = lname))

# starting with the "modules" (works as a combination of functions, as I understood)
# there is different ways to call modules:
# import helpers
# helpers.display("Not a warning!")

# from helpers import *
# display("Not a warning!")

from helpers import display
display("Not a warning!")
display("wow", True)

# in the same module, we can define a lot of functions
from helpers import display, print_time2
print_time2()
print_time2("another message")

# packages: https://pypi.org/ (python package index)
# how to install packages?

# individually
# pip install colorama

# from a list of packages
# pip install -r requirements.txt

# should I work always with a virtual environment? i guess so, but dont get it
# to read later: https://towardsdatascience.com/virtual-environments-104c62d48c54

