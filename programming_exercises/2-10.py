# Variables
cookies = 0.0
sugar = 0.0
butter = 0.0
flour = 0.0

# Constants
COOKIES_RECIPE = 48.0
SUGAR_RECIPE = 1.5
BUTTER_RECIPE = 1.0
FLOUR_RECIPE = 2.75

# Get number of cookies
cookies = float(input("Enter the number of cookies: "))

# Calculate the cups of sugar
sugar = (cookies * SUGAR_RECIPE) / COOKIES_RECIPE

# Calculate the cups of butter needed
butter = (cookies * BUTTER_RECIPE) / COOKIES_RECIPE

# Calculate the cups of flour needed
flour = (cookies * FLOUR_RECIPE) / COOKIES_RECIPE

# Print the amounts
print("To make", cookies, "cookies, you will need: ")
print(format(sugar, '.2f'), "cups of sugar")
print(format(butter, '.2f'), "cups of butter")
print(format(flour, '.2f'), "cups of flour")