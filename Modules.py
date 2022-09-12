# Modules contain sets of functions that can be useful for many different things.
# To use the functions within them you must import them.

# There are three different ways to do this.
# Generic imports function imports and universal imports.

# Generic Import
import random  # random has random integer and floats

print(random.randint(1, 10))

# Function Import
from random import randint

print(randint(10, 20))

# Universal Import
from random import *

print(random())
# the random function is a function imported from the random module which returns a float that is greater
# than or equal to zero point zero and less than 1.0 when it is called.

# ==========================================================================================================

# Miles per Gallon CHALLENGE
from random import randint
fuel = randint(10, 25)
miles = randint(200, 400)

print("The car can travel " + str(miles // fuel) + " miles per gallon.")

print("The car's fuel tank can hold " + str(fuel) + " gallons.")

print("The car can travel " + str(miles) + " miles on a full tank.")