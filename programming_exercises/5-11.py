import random

def generate_quiz():
    # generate two random numbers between 1 and 100
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # calculate the correct answer
    correct_answer = num1 + num2
    return num1, num2, correct_answer

def main():
    # welcome
    print("Welcome to the simple math quiz!")
    num1, num2, correct_answer = generate_quiz()
    print(f"\n  {num1}\n+ {num2}")

    # get the user's answer
    user_answer = int(input("Enter your answer: "))

    # check if the answer is correct
    if user_answer == correct_answer:
        print("Congratulations! Your answer is correct.")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")

if __name__ == "__main__":
    main()