def main():
    # get replacement cost from the user
    replacement_cost = float(input("Enter the replacement cost: "))

    # Calculate the minimum insurance amount (80% of replacement cost)
    minimum_insurance = 0.8 * replacement_cost

    # Display the min insurance amount
    print("You should buy a minimum of $", format(minimum_insurance, '.2f'), " in insurance")

if __name__ == "__main__":
    main()