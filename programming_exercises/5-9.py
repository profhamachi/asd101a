def main():
    # get the total sales for the month from the user
    total_sales = float(input("Enter the total sales for the month: $"))

    # constants for tax rates
    state_tax_rate = 0.05
    county_tax_rate = 0.025

    # calculate the amount of county sales tax
    county_sales_tax = total_sales * county_tax_rate

    # calculate the amount of state sales tax
    state_sales_tax = total_sales * state_tax_rate

    # calculate the total sales tax
    total_sales_tax = county_sales_tax + state_sales_tax

    # display the results
    print("\nAmount of County Sales Tax: $", format(county_sales_tax, ".2f"))
    print("Amount of State Sales Tax: $", format(state_sales_tax, ".2f"))
    print("Total Sales Tax: $", format(total_sales_tax, ".2f"))

if __name__ == "__main__":
    main()