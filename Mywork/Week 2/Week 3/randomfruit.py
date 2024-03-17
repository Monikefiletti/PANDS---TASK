# This program prints out a random fruit, I just replaced for colours

import random

colours = ['red', 'Black', 'Green', 'Purple']

# we want a random number between 0 and lenght-1

index = random.randint(0,len(colours)-1)
colours = colours[index]
print("A Random Colour:{}".format(colours))