print('Enter the starting principal: ', end='')
p = float(input())

print('Enter the annual interest rate: ', end='')
r = float(input())

print('How many times per year is the interest compounded? ', end='')
n = int(input())

print('For how many years will the account earn interest? ', end='')
t = int(input())

# Adjust the interest rate.
r = r / 100

# Calculate the ending balance.
a = p * (1 + float(r) / n) ** (n * t)

# Display the ending balance.
print('At the end of', t, 'years you will have $', format(a, ',.2f'))