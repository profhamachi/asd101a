# Variables to hold the prices of each item, the subtotal,
# and the total.
item1 = 0.0
item2 = 0.0
item3 = 0.0
item4 = 0.0
item5 = 0.0
tax = 0.0
total = 0.0

# Constant for the sales tax rate.
TAX_RATE = 0.07

# Get the price of each item
item1 = float(input("Enter the price of item #1: "))
item2 = float(input("Enter the price of item #2: "))
item3 = float(input("Enter the price of item #3: "))
item4 = float(input("Enter the price of item #4: "))
item5 = float(input("Enter the price of item #5: "))

# Calculate the subtotal
subtotal = item1 + item2 + item3 + item4 + item5

# Calculate the sales tax.
tax = subtotal * TAX_RATE

# Calculate the total.
total = subtotal + tax

# Print the values
print("Subtotal: ", format(subtotal, '.2f'))
print("Sales Tax: ", format(tax, '.2f'))
print("Total: ", format(total, '.2f'))