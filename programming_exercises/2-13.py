# This program calculates the number of grapevines
# that can be planted in a vineyard row.

print('Enter the length of the row, in feet: ', end='')
r = float(input())

print('Enter the amount of space, in feet, used by an end-post assembly: ', end='')
e = float(input())

print('Enter the distance, in feet, between each vine: ', end='')
s = float(input())

# Calculate
v = (r - 2 * e) / s

print('You have enough space for', v, 'vines.')