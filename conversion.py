#!/usr/bin/env python3

# used for 'surprise me' option
from http.client import SWITCHING_PROTOCOLS
from nis import match
import random
from secrets import choice
from unittest import case

# import helper library
from helpers import length
from helpers import temperature


def main_menu():
    Exit = False
    while (Exit != True):
        print("What conversion would you like to perform?\n"
            + "1. Temperature Conversion\n"
                + "2. Imperial to Metric (and reverse)\n"
                + "3. Surprise me!\n"
                + "4. Exit\n")

        choice = input()
        if choice == '1':
            temperature_menu()
        elif choice == '2':
            length.kmToMiles
        elif choice == '3':
            print("This is the random generator placeholder\n")
        elif choice == '4':
            Exit = True
        else:
            print("That is not a valid choice, please select again.\n")


def temperature_menu():
    print("What temperature unit would you like to convert?\n"
          + "1. Fahrenheit to Celsius\n"
            + "2. Fahrenheit to Kelvin\n"
            + "3. Celsius to Fahrenheit\n"
            + "4. Celsius to Kelvin\n"
            + "5. Kelvin to Fahrenheit\n"
            + "6. Kelvin to Celsius\n"
            + "7. Back\n")

    choice = input()
    if choice == '1':
        fahr = int(input("What is the temperature in fahrenheit?\nEnter: "))
        temperature.fahrenheit_celsius(fahr)
    elif choice == '2':
        fahr = int(input("What is the temperature in fahrenheit?\nEnter: "))
        temperature.fahrenheit_kelvin(fahr)
    elif choice == '3':
        print("C to F\n")
    elif choice == '4':
        print("C to K\n")
    elif choice == '5':
        print("K to F\n")
    elif choice == '6':
        print("K to C\n")
    elif choice == '7':
        main_menu()
    else:
        print("That is not a valid choice, please select again.\n")


def main():
    print("Welcome to the Py Conversion Tool!")
    main_menu()
    exit()

if __name__ == "__main__":
    main()
