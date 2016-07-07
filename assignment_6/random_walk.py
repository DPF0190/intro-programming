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


def get_direction_displacement(dir_key):
    displacements = {
        'west': (-1, 0),
        'east': (1, 0),
        'north': (0, 1),
        'south': (0, -1)
        }
    return displacements[dir_key]

def take_walk(steps):
    current_location = [0, 0]
    for step_index in range(steps):
        direction = get_random_direction()

        displacement = get_direction_displacement(direction)

        # extract the numerical values from the tuple
        delta_x = displacement[0]
        delta_y = displacement[1]

        example_location = [0, 0]
        change_in_x = -1
        change_in_y = 0
        example_location[0] += change_in_x
        example_location[1] += change_in_y

# UPDATE current_location HERE
        # consult example in 'Storing and Updating State' for method to update
        # current_location

    return current_location
