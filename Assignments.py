import os
import sys
import math

print("The current python version is:", sys.version)

libraries = ['os', 'sys', 'math', 'wow']
for lib in libraries:
    try:
        __import__(lib)
        print(f"{lib} is installed.")
    except ImportError:
        print(f"{lib} is not installed.")