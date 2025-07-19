#Module 1 - Assignment 1
firstname = str(input("Enter your first name: ")).strip()
lastname = str(input("Enter your last name: ")).strip()
print("Hello, " + firstname + " " + lastname + "! Welcome to Python programming.")

#Module 1 - Assignment 2
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("Before swapping a:", a, "b:", b)
a , b = b, a
print("After swapping a:",a,"b:", b)

#Module 1 - Assignment 2 - Using AI
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("Before swapping a:", a, "b:", b)
temp = a
a = b
b = temp
print("After swapping a:", a, "b:", b)

#Module 1 - Assignment 3
import sys
import os
import math

print("Python version installed on this system:")
print(sys.version)

print("\nChecking availability of commonly used libraries:")
libraries = {
    "os": os,
    "sys": sys,
    "math": math
}

for lib_name, lib in libraries.items():
    if lib:
        print(f"Library '{lib_name}' is available and loaded.")
    else:
        print(f"Library '{lib_name}' is not available.")
        

