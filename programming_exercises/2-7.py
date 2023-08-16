# Variables
miles = 0.0
gallons = 0.0
mpg = 0.0

# Get miles driven
miles = float(input("Enter the miles driven: "))

# Get gallons used
gallons = float(input("Enter the gallons of fuel used: "))

# Calculate MPG
mpg = miles / gallons

# Print the result.
print("You used", format(mpg, '.2f'), "miles per gallon.")