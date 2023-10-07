
# Modify the line below
age = int(input('What is your age? '))

print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# Modify the line below
height = float(input('What is your height in meters? '))

print(f"Type of height variable is: {type(height)}. It should be <class 'float'>")

# Modify the line below
loyalty_input = input('Are you part of our loyalty program? ')
loyalty = loyalty_input.lower() == 'yes' or loyalty_input.lower() == 'true'

print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")
