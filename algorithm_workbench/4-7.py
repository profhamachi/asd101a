num_rows = 10
num_chars_per_row = 15

# outer loop
for i in range(num_rows):
    # inner loop
    for j in range(num_chars_per_row):
        print("#", end="")
    # after printing a row, print one more for good measure
    print()