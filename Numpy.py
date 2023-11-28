import numpy as np

# a. all zeros
zeros_array = np.zeros((4, 3))

# b. ones
ones_array = np.ones((4, 3))

# c. numbers from 0 to 11
range_array = np.arange(12).reshape((4, 3))

print("Array with all zeros:")
print(zeros_array)

print("\nArray with all ones:")
print(ones_array)

print("\nArray with numbers from 0 to 11:")
print(range_array)

##
x_values = np.arange(1, 101, 1)
function_values = 2 * x_values**2 + 5

print("x values:")
print(x_values)

print("\nFunction values:")
print(function_values)

##
x_values_exp = np.arange(-10, 11, 1)
function_values_exp = np.exp(-x_values_exp)

print("x values for exponential function:")
print(x_values_exp)

print("\nFunction values for exponential function:")
print(function_values_exp)