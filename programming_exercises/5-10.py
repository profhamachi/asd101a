def feet_to_inches(feet):
    inches = feet * 12
    return inches

def main():
    # get the number of feet from the user
    feet = float(input("Enter number of feet: "))

    # call the feet_to_inches function to convert feet to inches
    inches = feet_to_inches(feet)

    # display the results
    print(f"{feet} feet is equal to {inches} inches")

if __name__ == "__main__":
    main()