#!/usr/bin/env python3

# Created by: Noah
# Created on: April 2022
# This program guesses a random number

import Constants


def main():

    # This is a random number guesser

    # input
    random_number = int(input("Enter your first guess here (0-9): "))

    # process & output
    if random_number != Constants.guess_number:
        print("Guess is incorrect")
    if random_number == Constants.guess_number:
        print("Guess is correct!")


if __name__ == "__main__":
    main()
