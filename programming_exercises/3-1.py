number = input("Enter a number between 1 and 7: ")

if number.isdigit():
    number = int(number)
    if 1 <= number <= 7:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_of_week = days[number -1]
        print(f"The corresponding day of the week is: {day_of_week}")
    else:
        print("Error: The number should be between 1 and 7.")
else:
    print("Error: Please enter a valid number.")