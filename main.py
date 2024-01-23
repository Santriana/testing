# import module already created
import my_module

# use the function from module
message = my_module.greet('Alice')
print(message)

# Use variable from module
radius = 5
area = my_module.pi * my_module.square(radius)
print(f'Luas lingkaran dengan radius {radius} adalah {area:.2f}')