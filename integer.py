#!/usr/bin/env python3\
# Created By:Kamche
# Created on: October 9, 2026
# This program asks the user for an integer
# and checks whether the number is positive
# negative or equal to zero.
import integer


def main():
    # ask the user for a number that is an integer
    number = int(input("Enter a number that is an integer: "))

    # check if the number is positive or negative or equal to zero
    if number > 0:
        print("{0} \nYour number is a positive value of an integer.".format(number))
    elif number < 0:
        print("{0} \nYour number is a negative value of an integer.".format(number))
    else:
        print("{0} \nYour number is equal to zero.".format(number))


if __name__ == "__main__":
    main()
