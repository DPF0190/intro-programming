import random

def get_random_direction():
    direction = " "
    probability = random.random()

    if probability < 0.25:
        direction = "west"
    elif probability < 0.5: 
	direction = "north"
    elif probability < 0.75:
	direction = "south"
    else:
	direction = "east"

    return direction

print(get_random_direction())
print(get_random_direction())
print(get_random_direction())
print(get_random_direction())
print(get_random_direction())
print(get_random_direction())
print(get_random_direction())
print(get_random_direction())
