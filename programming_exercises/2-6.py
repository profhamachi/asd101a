# Variables
purchase = 0.0
stateTax = 0.0
countyTax = 0.0
totalTax = 0.0
totalSale = 0.0

# Constants for state and county tax rates
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Get the amount of the purchase
purchase = float(input("Enter the amount of the purchase: "))

# Calculate the state sales tax.
stateTax = purchase * STATE_TAX_RATE

# Calculate the county sales tax.
countyTax = purchase * COUNTY_TAX_RATE

# Calculate the total tax.
totalTax = stateTax + countyTax

# Calculate the total of the sale.
totalSale = purchase + totalTax

# Print information about the sale.
print("Purchase Amount: \t", format(purchase, '.2f'))
print("State Tax: \t\t", format(stateTax, '.2f'))
print("County Tax: \t\t", format(countyTax, '.2f'))
print("Total Tax: \t\t", format(totalTax, '.2f'))
print("Total Sale: \t\t", format(totalSale, '.2f'))