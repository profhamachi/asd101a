import random

def main():
    # initialize counters for even and odd numbers
    even_count = 0
    odd_count = 0

    # generate and check 100 random numbers
    for _ in range(100):
        random_number = random.randint(1, 100)
        if random_number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # display results
    print("Number of even numbers:", even_count)
    print("Number of odd numbers:", odd_count)

if __name__ == "__main__":
    main()