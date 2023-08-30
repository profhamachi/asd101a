# function to calculate the average of five test scores
def calc_average(score1, score2, score3, score4, score5):
    total = score1 + score2 + score3 + score4 + score5
    average = total / 5
    return average

# function to determine the letter grade based on a test score
def determine_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
def main():
    # get five test scores from the user
    score1 = int(input("Enter the first test score: "))
    score2 = int(input("Enter the second test score: "))
    score3 = int(input("Enter the third test score: "))
    score4 = int(input("Enter the fourth test score: "))
    score5 = int(input("Enter the fifth test score: "))

    # calculate the average test score using the calc_average function
    average_score = calc_average(score1, score2, score3, score4, score5)

    # display the letter grade for each score and the average test score
    print("\nTest Scores and Letter Grades:")
    print(f"Score 1: {score1} - Grade: {determine_grade(score1)}")
    print(f"Score 2: {score2} - Grade: {determine_grade(score2)}")
    print(f"Score 3: {score3} - Grade: {determine_grade(score3)}")
    print(f"Score 4: {score4} - Grade: {determine_grade(score4)}")
    print(f"Score 5: {score5} - Grade: {determine_grade(score5)}")
    print(f"Average Test Score: {average_score:.2f} - Grade: {determine_grade(average_score)}")

if __name__ == "__main__":
    main()