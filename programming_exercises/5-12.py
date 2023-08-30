# function to find the max of two integers
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    # get two integer values from the user
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    # call the max function to find the greater value
    result = max(num1, num2)

    # display the results
    print("The greater value is: ", result)

if __name__ == "__main__":
    main()