amount1 = 11
amount2 = 99

if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
            print("The greater amount is: ", amount1)
        else:
            print("The greater amount is: ", amount2)
    else:
        print("amount2 is not less than 100.")
else:
    print("amount1 is not greater than 10.")