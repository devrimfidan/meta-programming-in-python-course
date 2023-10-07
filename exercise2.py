# The below script will ask for 3 inputs. Each input will be based
# on the price of the items - the price is determined by you. The output
# should print the total of the 3 inputs rounded to 2 decimal places e.g
#
#   1 coffee @ $ 2.00
#   1 sandwich @ $ 4.99
#   1 cake @ $ 2.75
#
#   Your total bill is $ 9.74

# Convert input to float
coffee = float(input('1 coffee @: $ '))

# Convert input to float
sandwich = float(input('1 sandwich @: $ '))

# Convert input to float
cake = float(input('1 cake @: $ '))

# Calculate the total bill
bill_total = coffee + sandwich + cake

# Format and print the total bill rounded to 2 decimal places
print(f'1 coffee @ $ {coffee:.2f}')
print(f'1 sandwich @ $ {sandwich:.2f}')
print(f'1 cake @ $ {cake:.2f}')
print(f'Your total bill is ${bill_total:.2f}')
