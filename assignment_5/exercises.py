import math

def gravity(gravity):
    # gravity isn't going to change, units in m/(s^2)
    gravity = 9.8

def height(height):
    height = (1/2) * gravity * time * time

def time(time):
    time = math.sqrt((2 * height) / gravity)
    return time    

print(time(10))









 






