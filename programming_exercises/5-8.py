def main():
    # get the square feet of wall space to be pained
    square_feet = float(input("Enter the square feet of wall space to be painted: "))

    # get the price of paint per gallon
    paint_price_per_gallon = float(input("Enter the price of paint per gallon: "))

    # constants
    square_feet_per_gallon = 112
    hours_per_gallon = 8
    labor_rate_per_hour = 35.00

    # calculate the number of gallons of paint required
    gallons_of_paint = square_feet / square_feet_per_gallon

    # calculate the hours of labor required
    hours_of_labor = gallons_of_paint * hours_per_gallon

    # calculate the cost of the paint
    paint_cost = gallons_of_paint * paint_price_per_gallon

    # calculate the labor charges
    labor_charges = hours_of_labor * labor_rate_per_hour

    # calculate the total cost of the paint job
    total_cost = paint_cost + labor_charges

    # display the results
    print("\nNumber of Gallons of Paint Required: ", gallons_of_paint)
    print("Hours of labor required: ", format(hours_of_labor, ".2f"))
    print("Cost of Paint: $", format(paint_cost, ".2f"))
    print("Labor Charges: $", format(labor_charges, ".2f"))
    print("Total Cost of the Paint Job: $", format(total_cost, ".2f"))

if __name__ == "__main__":
    main()
