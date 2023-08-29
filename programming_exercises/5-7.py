def main():
    # define ticket prices
    class_a_price = 20
    class_b_price = 15
    class_c_price = 10

    # get the number of tickets sold for each class
    class_a_tickets = int(input("Enter the number of Class A tickets sold: "))
    class_b_tickets = int(input("Enter the number of Class B tickets sold: "))
    class_c_tickets = int(input("Enter the number of Class C tickets sold: "))

    # calculate the total income generated from ticket sales
    total_income = (class_a_tickets * class_a_price) + (class_b_tickets * class_b_price) + (class_c_tickets * class_c_price)

    # display the total income
    print("\nTotal Income from Ticket Sales: $", total_income)

if __name__ == "__main__":
    main()