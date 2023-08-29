def main():
    # get the number of fat grams and carbohydrate grams from the user
    fat_grams = float(input("Enter the number of fat grams consumed: "))
    carb_grams = float(input("Enter the number of carbohydrate grams consumed: "))

    # calculate the number of calories from fat (fat grams * 9)
    calories_from_fat = fat_grams * 9

    # calculate the number of calories from carbohydrates (carb grams * 4)
    calories_from_carbs = carb_grams * 4

    # display the results
    print("\nCalories from Fat: ", calories_from_fat, " calories")
    print("Calories from Carbs: ", calories_from_carbs, " calories")

if __name__ == "__main__":
    main()