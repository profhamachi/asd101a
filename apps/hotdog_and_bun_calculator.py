hotdogs_per_package = 10
buns_per_package = 8

people_count = int(input("Enter the number of people attending the cookout: "))
hotdogs_per_person = int(input("Enter the number of hot dogs each person will eat: "))

total_hotdogs_needed = people_count * hotdogs_per_person
total_buns_needed = people_count * hotdogs_per_person

hotdog_packages_needed = (total_hotdogs_needed + hotdogs_per_package -1) // hotdogs_per_package
bun_packages_needed = (total_buns_needed + buns_per_package -1) // buns_per_package

hotdogs_leftover = (hotdog_packages_needed * hotdogs_per_package) - total_hotdogs_needed
buns_leftover = (bun_packages_needed * buns_per_package) - total_buns_needed

print("\nMinimum number of packages of hot dogs required: ", hotdog_packages_needed)
print("Minimum number of packages of hot dog buns required: ", bun_packages_needed)
print("Number of hot dogs left over: ", hotdogs_leftover)
print("Number of hot dog buns left over: ", buns_leftover)