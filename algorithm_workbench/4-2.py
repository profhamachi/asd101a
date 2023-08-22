while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    total = num1 + num2

    # display the result
    print(f"The sum of {num1} and {num2} is: {total}")

    # ask if the user wants to run again
    again = input("Do you want to perform the operation again? (y/n) ")

    while again not in ('y', 'n'):
        print("Please enter 'y' or 'n'.")
        again = input("Do you want to perform the operation again? (y/n) ")

    if again == "n":
        break
    
