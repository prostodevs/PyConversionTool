#!/usr/bin/env python3
""" Alta3 Student Project | J Stowe
    Common Conversion Tool - Primary controller"""

# import for 3rd party libraries
import random
import sys
import time

# import helper library
from helpers import length
from helpers import temperature
from helpers import weight


def main_menu():
    """Primary options menu"""
    exit_chk = False
    while (exit_chk is not True):
        print("What conversion would you like to perform?\n"
              + "1. Temperature Conversion\n"
                + "2. Length Conversion\n"
                + "3. Weight Conversion\n"
                + "4. Surprise!\n"
                + "5. Exit\n")

        choice = input("Enter: ")
        if choice == '1':
            temperature_menu()
        elif choice == '2':
            length_menu()
        elif choice == '3':
            weight_menu()
        elif choice == '4':
            surprise()
        elif choice == '5':
            exit_chk = True
        else:
            print("That is not a valid choice, please select again.\n")
        print("\n")
        time.sleep(1)

def temperature_menu():
    """Temperature menu controller"""
    # input error handling (passes value to helper)
    def try_catch(temp_unit):
        while True:
            try:
                entry = float(
                    input(f"What is the temperature in {temp_unit}?\nEnter: "))
            except ValueError:
                print("That is not a valid number!!")
            else:
                return entry

    menu = False
    while (menu is not True):
        print("What temperature unit would you like to convert?\n"
              + "1. Fahrenheit to Celsius\n"
                + "2. Fahrenheit to Kelvin\n"
                + "3. Celsius to Fahrenheit\n"
                + "4. Celsius to Kelvin\n"
                + "5. Kelvin to Fahrenheit\n"
                + "6. Kelvin to Celsius\n"
                + "7. Main Menu\n")

        choice = input("Enter:")
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
        print("\n")
        time.sleep(2)

def length_menu():
    """Length conversion controller"""
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
        choice_one = int(input("Enter: "))

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
        choice_two = int(input("Enter: "))
        length.length_menu[choice_one][choice_two]()
        print("\n")
        time.sleep(2)

def weight_menu():
    """Weight conversion controller"""
    while True:
        print("What weight would you like to convert?\n"
              + "1. Ounces\n"
                + "2. Pounds\n"
                + "3. Tons\n"
                + "4. Grams\n"
                + "5. Kilograms\n"
                + "6. Tonnes\n"
                + "7. Main Menu\n")
        choice_one = int(input("Enter: "))

        if choice_one == 7:
            break

        print("\nAnd what are you converting to?\n"
              + "1. Ounces\n"
                + "2. Pounds\n"
                + "3. Tons\n"
                + "4. Grams\n"
                + "5. Kilograms\n"
                + "6. Tonnes\n")
        choice_two = int(input("Enter: "))
        weight.weight_menu[choice_one][choice_two]()
        print("\n")
        time.sleep(2)

def surprise():
    """Surprise option menu"""
    print("This will be a surprise!!!")

def main():
    """Main execution"""
    print("Welcome to the Py Conversion Tool!")
    main_menu()
    print("Thank you for using the Py Conversion Tool!\n"
        + "Have a lovely day!\n")
    sys.exit()

if __name__ == "__main__":
    main()
