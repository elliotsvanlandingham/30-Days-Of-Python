'Day 2: 30 Days of python programming'
# Variables in Python

from os import remove, replace


first_name = 'Elliot'
last_name = 'VanLandingham'
full_name = f"{first_name} {last_name}"
country = 'USA'
city = 'Anna'
age = 29
year = 2026
is_married = 'yes'
is_true = True
is_light_on = 'yes'
personal_info = {
    'first_name': first_name,
    'last_name': last_name,
    'full_name': full_name,
    'country': country,
    'city': city,
    'age': age,
    'year': year,
    'is_married': is_married,
}
first_name, last_name, country, city = 'Elliot', 'VanLandingham', 'USA', 'Anna'
age, year = 29, 2026
full_name = f"{first_name} {last_name}"

# Check data type for all variables

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
# Print values stored in Variables

print(first_name)
print(last_name)
print('full name',full_name)
print(country)
print(city)
print(age)
print(year)
print('is married', is_married)
print('is true', is_true)
print('is light on', is_light_on)

print('length of first name:', len(first_name))
print('length of last name:', len(last_name))
print('length of full name (no spaces):', len(full_name.replace(' ', '')))

num_one = 5
num_two = 4
variable_total = num_one + num_two
print('variable total:', variable_total)

variable_diff = num_two - num_one
print('variable difference:', variable_diff)

variable_product = num_one * num_two
print('variable product:', variable_product)

variable_division = num_one / num_two
print('variable division:', variable_division)

variable_remainder = num_two % num_one
print('variable remainder:', variable_remainder)

variable_exp = num_one ** num_two
print('variable exponent:', variable_exp)

variable_floor_division = num_one // num_two
print('variable floor division:', variable_floor_division)

# Calculate the radius of a circle

import math
radius = 30
pi = math.pi

area_of_circle = pi * radius ** 2
print('area of circle:', area_of_circle, 'meters')

circum_of_circle = 2 * math.pi * radius
print('circumference of circle:', circum_of_circle, 'meters')

area_of_circle = math.pi * (radius ** 2)
print('area of circle:', area_of_circle, 'meters')

# --- LEVEL 2: The user types the number ---
user_radius = float(input('Enter the radius of the circle: '))
user_area = math.pi * (user_radius ** 2)
print('The area of the circle', 'is:', user_area, 'meters', 'for a circle with a radius of', user_radius, 'meters')

# Gathering user information
first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
country = input('Enter country: ')
age = int(input('Enter age: '))

# Printing the stored variables to verify they work
print('--- User Information ---')
print('First Name:', first_name)
print('Last Name:', last_name)
print('Country:', country)
print('Age:', age)


help('keywords')

