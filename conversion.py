#!/usr/bin/env python3

# used for 'surprise me' option
import random

# import helper library
from helpers import length
from helpers import temperature


def main_menu():
    Exit = False
    while (Exit != True):
        print("What conversion would you like to perform?\n"
              + "1. Temperature Conversion\n"
                + "2. Length Conversion\n"
                + "3. Weight Conversion\n"
                + "4. Surprise!\n"
                + "5. Exit\n")

        choice = input()
        if choice == '1':
            temperature_menu()
        elif choice == '2':
            length_menu()
        elif choice == '3':
            weight_menu()
        elif choice == '4':
            surprise()
        elif choice == '5':
            Exit = True
        else:
            print("That is not a valid choice, please select again.\n")


def temperature_menu():
    # input error handling (passes value to helper)
    def try_catch(temp_unit):
        while True:
            try:
                entry = float(
                    input("What is the temperature in {temp_unit}?\nEnter: "))
            except ValueError:
                print("That is not a valid number!!")
            else:
                return entry

    menu = False
    while (menu != True):
        print("What temperature unit would you like to convert?\n"
              + "1. Fahrenheit to Celsius\n"
                + "2. Fahrenheit to Kelvin\n"
                + "3. Celsius to Fahrenheit\n"
                + "4. Celsius to Kelvin\n"
                + "5. Kelvin to Fahrenheit\n"
                + "6. Kelvin to Celsius\n"
                + "7. Main Menu\n")

        choice = input()
        if choice == '1':
            temperature.fahrenheit_celsius(try_catch('Fahrenheit'))
        elif choice == '2':
            temperature.fahrenheit_kelvin(try_catch('Fahrenheit'))
        elif choice == '3':
            temperature.celsius_fahrenheit(try_catch('Celsius'))
        elif choice == '4':
            temperature.celsius_kelvin(try_catch('Celsius'))
        elif choice == '5':
            temperature.kelvin_fahrenheit(try_catch('Kelvin'))
        elif choice == '6':
            temperature.kelvin_celsius(try_catch('Kelvin'))
        elif choice == '7':
            menu = True
        else:
            print("That is not a valid choice, please select again.\n")


def length_menu():
    while True:
        print("What length unit would you like to convert?\n"
              + "1. Inches\n"
                + "2. Feet\n"
                + "3. Yards\n"
                + "4. Miles\n"
                + "5. Millimeters\n"
                + "6. Meters\n"
                + "7. Kilometers\n"
                + "8. Main Menu\n")
        choice_one = int(input())

        if choice_one == 8:
            break

        print("\nAnd what are you converting to?\n"
              + "1. Inches\n"
                + "2. Feet\n"
                + "3. Yards\n"
                + "4. Miles\n"
                + "5. Millimeters\n"
                + "6. Meters\n"
                + "7. Kilometers\n")
        choice_two = int(input())

        length.list[choice_one][choice_two]()


def weight_menu():
    print("This is the weight menu")


def surprise():
    print("This will be a surprise!!!")


def main():
    print("Welcome to the Py Conversion Tool!")
    main_menu()
    print("Thank you for using the Py Conversion Tool!\n"
          + "Have a lovely day!")
    exit()


if __name__ == "__main__":
    main()
