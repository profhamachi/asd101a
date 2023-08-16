# Variables for the number of male and female students,
# total number of students, and the percentage of male
# and female students.
male = 0
female = 0
total = 0
percentMale = 0.0
percentFemale = 0.0

# get the number of male students.
male = int(input("Enter the number of male students: "))

# get the number of female students.
female = int(input("Enter the number of female students: "))

# Calculate the number of students.
total = male + female

# get the percentage of male students.
percentMale = male / total

# get the percentage of female students.
percentFemale = female / total

# Print the percentage of male students.
print("Male: ", format(percentMale, '.2f'), "%")

# Print the percentage of female students.
print("Female: ", format(percentFemale, '.2f'), "%")
