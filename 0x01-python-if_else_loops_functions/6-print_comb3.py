#!/usr/bin/python3
for First_digit in range(0, 10):
    for Second_digit in range(First_digit + 1, 10):
        if First_digit == 8 and Second_digit == 9:
            print("{}{}".format(First_digit, Second_digit))
        else:
            print("{}{}".format(First_digit, Second_digit), end=", ")
