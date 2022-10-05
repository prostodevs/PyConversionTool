#!/usr/bin/env python3

# used for 'surprise me' option
import random
from secrets import choice

# import helper library
from helpers import length


def main_menu():
    print("What conversion would you like to perform?\n"
          + "1. Temperature Conversion\n"
          + "2. Imperial to Metric (and reverse)\n"
          + "3. Surprise me!\n"
          + "4. Exit\n")


def main():
    print("Welcome to the Py Conversion Tool!")

    Exit = False
    while (Exit != True):
        main_menu()

        choice = input()
        if choice == '1':
            print("temperature placeholder\n")
        elif choice == '2':
            length.kmToMiles
        elif choice == '3':
            print("This is the random generator placeholder\n")
        elif choice == '4':
            Exit = True
        else:
            print("That is not a valid choice, please select again.\n")


if __name__ == "__main__":
    main()
