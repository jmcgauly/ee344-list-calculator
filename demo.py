"""Run this example with: python demo.py"""

from labtools import add, multiply, add_numpy, multiply_numpy

numbers = [1, 2, 3, 4]
print("Numbers:", numbers)
print("Sum:", add(numbers))

# Assignment 1: implement multiply, then print its result here.
print("Product:", multiply(numbers))
# Assignment 2: import and call your add_numpy and multiply_numpy functions here.
print("NumPy sum:", add_numpy(numbers))
print("NumPy product:", multiply_numpy(numbers))