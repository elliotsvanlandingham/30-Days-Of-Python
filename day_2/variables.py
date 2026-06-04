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
