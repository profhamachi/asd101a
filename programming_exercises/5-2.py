# Get the amount of the purchase
def get_purchase_amount():
    return float(input("Enter the amount of the purchase: "))

# Function to calculate the state sales tax.
def calculate_state_tax(purchase_amount):
    return purchase_amount * STATE_TAX_RATE

# Calculate the county sales tax.
def calculate_county_tax(purchase_amount):
    return purchase_amount * COUNTY_TAX_RATE

# Calculate the total tax.
def calculate_total_tax(state_tax, county_tax):
    return state_tax + county_tax

# Calculate the total of the sale.
def calculate_total_sale(purchase_amount, total_tax):
    return purchase_amount + total_tax

# Print information about the sale.
def print_sale_info(purchase_amount, state_tax, county_tax, total_tax, total_sale):
    print("Purchase Amount: \t", format(purchase_amount, '.2f'))
    print("State Tax: \t\t", format(state_tax, '.2f'))
    print("County Tax: \t\t", format(county_tax, '.2f'))
    print("Total Tax: \t\t", format(total_tax, '.2f'))
    print("Total Sale: \t\t", format(total_sale, '.2f'))

# Constants for state and county tax rates
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

def main():
    # Get the amount of the purchase
    purchase_amount = get_purchase_amount()

    # Calculate the state sales tax
    state_tax = calculate_state_tax(purchase_amount)

    # Calculate the county sales tax
    county_tax = calculate_county_tax(purchase_amount)

    # Calculate the total tax
    total_tax = calculate_total_tax(state_tax, county_tax)

    # Calculate the total sale
    total_sale = calculate_total_sale(purchase_amount, total_tax)

    # Print information about the sale
    print_sale_info(purchase_amount, state_tax, county_tax, total_tax, total_sale)

if __name__ == "__main__":
    main()