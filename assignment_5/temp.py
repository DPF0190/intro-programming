def to_fahrenheit(degrees_celsius):
    output = degrees_celsius * (9/5) + 32
    return output

def to_celsius(degrees_fahrenheit):
    output = (degrees_fahrenheit - 32) * 5/9
    return output
 
print(to_fahrenheit(0))
print(to_fahrenheit(50))
print(to_fahrenheit(100))
print(to_fahrenheit(150))


print(to_celsius(0))
print(to_celsius(50))
print(to_celsius(100))
print(to_celsius(150))


