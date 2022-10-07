#!/usr/bin/env python3
""" Alta3 Student Project | J Stowe
    Length Conversion Controller """

def try_catch():
    """User input error handling"""
    is_valid = False
    while (is_valid is not True):
        try:
            entry = float(
                input("\nWhat is the input length?\nEnter: "))
        except ValueError:
            print("That is not a valid number!!")
        else:
            is_valid = True
            return entry

## string function to satisfy dict call in conversion.py
def str_call():
    """String placeholder for 1:1 conversion in dictionary"""
    print("You already know that!!")

## 1:inch conversion functions
def inch_feet():
    user_input = try_catch()
    feet = user_input * (1 / 12)
    print(f"{user_input} inches is {feet:.2f} feet.")

def inch_yards():
    user_input = try_catch()
    yards = input * (1 / (12 * 3))
    print(f"{user_input} inches is {yards:.3f} yards")


def inch_miles():
    user_input = try_catch()
    miles = user_input * (1 / (12 * 5280))
    print(f"{user_input} inches is {miles:.4f} miles.")


def inch_millimeters():
    user_input = try_catch()
    millimeters = user_input * (25.4 / 1)
    print(f"{user_input} inches is {millimeters:.5f} millimeters.")


def inch_meters():
    user_input = try_catch()
    meters = user_input * (25.4 / 1000)
    print(f"{user_input} inches is {meters:.7f} meters.")


def inch_kilometers():
    user_input = try_catch()
    kilometers = user_input * (25.4 / 1000 / 1000)
    print(f"{user_input} inches is {kilometers:.9f} kilometers.")

## feet conversion functions
def feet_inches():
    user_input = try_catch()
    inches = user_input * (12 / 1)
    print(f"{user_input} inches is {inches:.2f} inches")


def feet_yards():
    user_input = try_catch()
    yards = user_input * (1 / 3)
    print(f"{user_input} inches is {yards:.4f} yards")


def feet_miles():
    user_input = try_catch()
    miles = user_input * (1 / 5280)
    print(f"{user_input} inches is {miles:.5f} miles")


def feet_millimeters():
    user_input = try_catch()
    millimeters = user_input * (304.8 / 1)
    print(f"{user_input} feet is {millimeters:.4f} millimeters")


def feet_meters():
    user_input = try_catch()
    meters = user_input * (304.8 / 1000)
    print(f"{user_input} feet is {meters:.4f} meters")


def feet_kilometers():
    user_input = try_catch()
    kilometers = user_input * (304.8 / 1000 / 1000)
    print(f"{user_input} kilometers is {kilometers:.4f} feet")


## yard conversion functions
def yards_inches():
    user_input = try_catch()
    inches = user_input * (36 / 1)
    print(f"{user_input} inches is {inches:.2f} inches")


def yards_feet():
    user_input = try_catch()
    feet = user_input * (3 / 1)
    print(f"{user_input} yards is {feet:.4f} feet")


def yards_miles():
    user_input = try_catch()
    miles = user_input * (1 / 1760)
    print(f"{user_input} yards is {miles:.5f} miles")


def yards_millimeters():
    user_input = try_catch()
    millimeters = user_input * (914.4 / 1)
    print(f"{user_input} yards is {millimeters:.4f} millimeters")


def yards_meters():
    user_input = try_catch()
    meters = user_input * (914.4 / 1000)
    print(f"{user_input} yards is {meters:.4f} meters")


def yards_kilometers():
    user_input = try_catch()
    kilometers = user_input * (914.4 / 1000 / 1000)
    print(f"{user_input} yards is {kilometers:.4f} feet")

## mile conversion functions
def miles_inches():
    user_input = try_catch()
    inches = user_input * (63360 / 1)
    print(f"{user_input} miles is {inches:.2f} inches")


def miles_feet():
    user_input = try_catch()
    feet = user_input * (5280 / 1)
    print(f"{user_input} miles is {feet:.4f} feet")


def miles_yards():
    user_input = try_catch()
    yards = user_input * (1760 / 1)
    print(f"{user_input} miles is {yards:.4f} miles")


def miles_millimeters():
    user_input = try_catch()
    millimeters = user_input * (1609344/ 1)
    print(f"{user_input} miles is {millimeters:.4f} millimeters")


def miles_meters():
    user_input = try_catch()
    meters = user_input * (1609344 / 1000)
    print(f"{user_input} yards is {meters:.4f} meters")


def miles_kilometers():
    user_input = try_catch()
    kilometers = user_input * (1609344 / 1000 / 1000)
    print(f"{user_input} miles is {kilometers:.4f} kilometers")

## millimeters conversion functions
def millimeters_inches():
    user_input = try_catch()
    inches = user_input * (1 / .03937)
    print(f"{user_input} millimeters is {inches:.2f} inches")


def millimeters_feet():
    user_input = try_catch()
    feet = user_input * (.0032808)
    print(f"{user_input} millimeters is {feet:.4f} feet")


def millimeters_yards():
    user_input = try_catch()
    yards = user_input * (.0010936)
    print(f"{user_input} millimeters is {yards:.7f} miles")


def millimeters_miles():
    user_input = try_catch()
    miles = user_input * (.00000062137)
    print(f"{user_input} millimeters is {miles:.9f} miles")


def millimeters_meters():
    user_input = try_catch()
    meters = user_input * (1 / 1000)
    print(f"{user_input} millimeters is {meters:.7f} meters")


def millimeters_kilometers():
    user_input = try_catch()
    kilometers = user_input * (1 / 1000 / 1000)
    print(f"{user_input} millimeters is {kilometers:.9f} kilometers")

## meters conversion functions
def meters_inches():
    user_input = try_catch()
    inches = user_input * (1 / .03937)
    print(f"{user_input} meters is {inches:.2f} inches")


def meters_feet():
    user_input = try_catch()
    feet = user_input * (.0032808)
    print(f"{user_input} meters is {feet:.4f} feet")


def meters_yards():
    user_input = try_catch()
    yards = user_input * (.0010936)
    print(f"{user_input} meters is {yards:.7f} miles")


def meters_miles():
    user_input = try_catch()
    miles = user_input * (.00000062137)
    print(f"{user_input} meters is {miles:.9f} miles")


def meters_millimeters():
    user_input = try_catch()
    millimeters = user_input * (1000 / 1)
    print(f"{user_input} meters is {millimeters:.7f} millimeters")


def meters_kilometers():
    user_input = try_catch()
    kilometers = user_input * (1 / 1000)
    print(f"{user_input} meters is {kilometers:.9f} kilometers")

## kilometers conversion functions
def kilometers_inches():
    user_input = try_catch()
    inches = user_input * (39369.6)
    print(f"{user_input} meters is {inches:.2f} inches")


def kilometers_feet():
    user_input = try_catch()
    feet = user_input * (3280.8)
    print(f"{user_input} meters is {feet:.4f} feet")


def kilometers_yards():
    user_input = try_catch()
    yards = user_input * (1093.6)
    print(f"{user_input} meters is {yards:.7f} miles")


def kilometers_miles():
    user_input = try_catch()
    miles = user_input * (.62137)
    print(f"{user_input} meters is {miles:.9f} miles")


def kilometers_millimeters():
    user_input = try_catch()
    millimeters = user_input * (1000 * 1000 / 1)
    print(f"{user_input} meters is {millimeters:.7f} millimeters")


def kilometers_meters():
    user_input = try_catch()
    meters = user_input * (1000 / 1)
    print(f"{user_input} meters is {meters:.9f} meters")

# dictionary for corresponding menu selections
length_menu = {
    1: {
        1: str_call,
        2: inch_feet,
        3: inch_yards,
        4: inch_miles,
        5: inch_millimeters,
        6: inch_meters,
        7: inch_kilometers

    },
    2: {
        1: feet_inches,
        2: str_call,
        3: feet_yards,
        4: feet_miles,
        5: feet_millimeters,
        6: feet_meters,
        7: feet_kilometers
    },
    3: {
        1: yards_inches,
        2: yards_feet,
        3: str_call,
        4: miles_yards,
        5: yards_millimeters,
        6: yards_meters,
        7: yards_kilometers
    },
    4: {
        1: miles_inches,
        2: miles_feet,
        3: miles_yards,
        4: str_call,
        5: miles_millimeters,
        6: miles_meters,
        7: miles_kilometers
    },
    5: {
        1: millimeters_inches,
        2: millimeters_feet,
        3: millimeters_yards,
        4: millimeters_miles,
        5: str_call,
        6: millimeters_meters,
        7: millimeters_kilometers
    },
    6: {
        1: meters_inches,
        2: meters_feet,
        3: meters_yards,
        4: meters_miles,
        5: meters_millimeters,
        6: str_call,
        7: meters_kilometers
    },
    7: {
        1: kilometers_inches,
        2: kilometers_feet,
        3: kilometers_yards,
        4: kilometers_miles,
        5: kilometers_millimeters,
        6: kilometers_meters,
        7: str_call
    },
}
