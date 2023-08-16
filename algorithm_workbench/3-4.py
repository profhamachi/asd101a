A_score = 90.00
B_score = 80.00
C_score = 70.00
D_score = 60.00

score = float(input("What is the grade in xx.xx format? "))

if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
