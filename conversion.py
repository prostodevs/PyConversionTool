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
        print("Select a conversion to perform:\n"
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

    menu_chk = False
    while (menu_chk is not True):
        print("Select the temperature unit to convert:\n"
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
            menu_chk = True
        else:
            print("That is not a valid choice, please select again.\n")
        print("\n")
        time.sleep(1.5)

def length_menu():
    """Length conversion controller"""
    
    # prompt user for starting unit of measurement
    while True:
        print("Enter the unit of length to convert?\n"
              + "1. Inches\n"
                + "2. Feet\n"
                + "3. Yards\n"
                + "4. Miles\n"
                + "5. Millimeters\n"
                + "6. Meters\n"
                + "7. Kilometers\n"
                + "8. Main Menu\n")

        # type error handling
        while True:
            try:
                choice_one = int(input("Enter 1-8: "))
            except:
                print("That is not a valid option, please try again.")
            else:
                break

        # break loop if user chooses 'Main Menu'
        if choice_one == 8:
            break

        # prompt for ending unit of measurement
        print("\nEnter the desired unit of length:\n"
              + "1. Inches\n"
                + "2. Feet\n"
                + "3. Yards\n"
                + "4. Miles\n"
                + "5. Millimeters\n"
                + "6. Meters\n"
                + "7. Kilometers\n")

        while True:
            try:
                choice_two = int(input("Enter 1-7: "))
            except:
                print("That is not a valid option, please try again.")
            else:
                break

        try:
            length.length_menu[choice_one][choice_two]()
        except:
            print("You did not make a valid selection!")

        print("\n")
        time.sleep(1)

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

        while True:
            try:
                choice_one = int(input("Enter 1-7: "))
            except:
                print("That is not a valid option, please try again.")
            else:
                break

        if choice_one == 7:
            break

        print("\nAnd what are you converting to?\n"
              + "1. Ounces\n"
                + "2. Pounds\n"
                + "3. Tons\n"
                + "4. Grams\n"
                + "5. Kilograms\n"
                + "6. Tonnes\n")

        while True:
            try:
                choice_two = int(input("Enter 1-6: "))
            except:
                print("That is not a valid option, please try again.")
            else:
                break
        
        try:
            weight.weight_menu[choice_one][choice_two]()
        except:
            print("You did not make a valid selection!")
        
        print("\n")
        time.sleep(1)

def surprise():
    """Surprise option menu"""
    surprise_int = random.randint(1,3)
    if surprise_int == 1:
        temperature_menu()
    elif surprise_int == 2:
        length_menu()
    else:
        weight_menu()

def main():
    """Main execution"""
    print("\nWelcome to the Py Conversion Tool!\n"
    + "This tool is designed to convert common units of measurement.")

    main_menu()
    
    print("Thank you for using the Py Conversion Tool!\n"
        + "We hope your experience was satisfactory.\n"
        + "Have a lovely day!\n")
    sys.exit()

if __name__ == "__main__":
    main()
