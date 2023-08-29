def main():
    # Get expenses
    loan_payment = float(input("Enter monthly loan payment: $"))
    insurance = float(input("Enter monthly insurance payment: $"))
    gas = float(input("Enter monthly gas cost: $"))
    oil = float(input("Enter monthly oil cost: $"))
    tires = float(input("Enter monthly tires cost: $"))
    maintenance = float(input("Enter monthly maintenance cost: $"))

    # Calculate the total monthly cost
    total_monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance

    # Calculate the total annual cost (12 times monthly)
    total_annual_cost = 12 * total_monthly_cost

    # Display the results
    print("\nTotal Monthly Cost: $", format(total_monthly_cost, ".2f"))
    print("Total Annual Cost: $", format(total_annual_cost, ".2f"))

if __name__ == "__main__":
    main()