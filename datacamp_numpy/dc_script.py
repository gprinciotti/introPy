# lists recap:
# powerful
# collection of values
# hold different types
# you can change, add, remove
# need for data science: mathematical operations over collections

# suppose you want to calcule body mass index (bmi) using two lists:
height = [1.73, 1.68, 1.71, 1.89, 1.79]
print(height)

weight = [65.4, 59.2, 63.6, 88.4, 68.7]
print(weight)

# weight / height ** 2 # you will get an error because python doesnt know how to make math with lists
# you dont want to calculate this for each person separately; so, you can use numpy

# numpy:
# numeric python
# alternative to python list: numpy array (remember that a numpy array contain only one type of information)
# allows calculations over entire arrays
# easy and fast!

import numpy as np

np_height = np.array(height)
print(np_height)

np_weight = np.array(weight)
print(np_weight)

bmi = np_weight / np_height ** 2 # easy and fast
print(bmi)

# its important to notice that a numpy array is a different type of object
# so, you should use specific methods with it
python_list = [1, 2, 3]
numpy_array = np.array(python_list)

print(python_list + python_list)
print(numpy_array + numpy_array)
# different types, different behavior!

# besides that, you can filter specific informations in numpy array like an normal list/array
print(bmi)
print(bmi[1])
print(bmi[0:2])
print(bmi > 23)
print(bmi[bmi > 23])

# datacamp exercises:

# first
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# second
height_in = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 74, 74, 69, 70]

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)

# third
weight_lb = [180, 215, 210, 210, 188, 176, 209, 200, 231, 180, 188, 180, 185, 160, 180, 185]

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)

# fourth
# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

# fifth
print(np.array([True, 1, 2]) + np.array([3, 4, False]))

# Options
print(np.array([True, 1, 2, 3, 4, False]))
print(np.array([4, 3, 0]) + np.array([0, 2, 2])) # correct answer
print(np.array([1, 1, 2]) + np.array([3, 4, -1]))
print(np.array([0, 1, 2, 3, 4, 5]))

# sixth

# Print out the weight at index 12
print(np_weight_kg[12])

# Print out sub-array of np_height_in: index 10 up to and including index 15
print(np_height_in[10:16])

# 2d numpy arrays: an improved list of lists
np_2d = np.array([height, weight])
print(np_2d)
print(np_2d.shape) # 2 rows, 5 columns

# subsetting
print(np_2d[0]) # select the row
print(np_2d[0][2]) # after select the row, you do another selection (in column)
print(np_2d[0, 2]) # you can use comma two (row, column)
print(np_2d[:,1:3]) # you arent selecting anything in row, but in columns
print(np_2d[1,:]) # you arent selecting anything in columns, but in rows