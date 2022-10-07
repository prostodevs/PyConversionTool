#!/usr/bin/env python3
""" Alta3 Student Project | J Stowe
    Weight Conversion Controller """

# error catching for user input
from helpers.length import str_call


def try_catch():
    """User input error handling"""
    is_valid = False
    while (is_valid is not True):
        try:
            entry = float(
                input("\nWhat is the input weight?\nEnter: "))
        except ValueError:
            print("That is not a valid number!!")
        else:
            is_valid = True
            return entry

# 1: conversion functions for ounces : others
def ounces_pounds():
    user_input = try_catch()
    pounds = user_input * (0.062500)
    print(f"{user_input} ounces is {pounds:.2f} pounds")


def ounces_tons():
    user_input = try_catch()
    tons = user_input * (0.000031250)
    print(f"{user_input} ounces is {tons:.9f} tons")


def ounces_grams():
    user_input = try_catch()
    grams = user_input / (.035274)
    print(f"{user_input} ounces is {grams:.2f} grams")


def ounces_kilograms():
    user_input = try_catch()
    kilograms = user_input / (35.274)
    print(f"{user_input} ounces is {kilograms:.9f} kilograms")


def ounces_tonnes():
    user_input = try_catch()
    tonnes = user_input / (35274)
    print(f"{user_input} ounces is {tonnes:.9f} tonnes")

# 2: conversion functions for pounds : others
def pounds_ounces():
    user_input = try_catch()
    ounces = user_input * (16)
    print(f"{user_input} pounds is {ounces:.2f} ounces")


def pounds_tons():
    user_input = try_catch()
    tons = user_input * (0.00050000)
    print(f"{user_input} pounds is {tons:.9f} tons")


def pounds_grams():
    user_input = try_catch()
    grams = user_input / (0.0022046)
    print(f"{user_input} pounds is {grams:.9f} grams")


def pounds_kilograms():
    user_input = try_catch()
    kilograms = user_input / (2.2046)
    print(f"{user_input} pounds is {kilograms:.9f} kilograms")


def pounds_tonnes():
    user_input = try_catch()
    tonnes = user_input / (2204.6)
    print(f"{user_input} pounds is {tonnes:.9f} tonnes")

# 3: conversion functions for tons : others


def tons_ounces():
    user_input = try_catch()
    ounces = user_input * (32000)
    print(f"{user_input} tons is {ounces:.2f} ounces")


def tons_pounds():
    user_input = try_catch()
    pounds = user_input * (2000)
    print(f"{user_input} tons is {pounds:.2f} pounds")


def tons_grams():
    user_input = try_catch()
    grams = user_input / (0.0000011023)
    print(f"{user_input} tons is {grams:.9f} grams")


def tons_kilograms():
    user_input = try_catch()
    kilograms = user_input / (.0011023)
    print(f"{user_input} tons is {kilograms:.9f} kilograms")


def tons_tonnes():
    user_input = try_catch()
    tonnes = user_input / (1.1023)
    print(f"{user_input} tons is {tonnes:.9f} tonnes")

# 4: conversion functions for grams : others


def grams_ounces():
    print()


def grams_pounds():
    print()


def grams_tons():
    print()


def grams_decigrams():
    print()


def grams_kilograms():
    print()


def grams_tonnes():
    print()

# 5: conversion functions for kilograms : others


def kilograms_ounces():
    print()


def kilograms_pounds():
    print()


def kilograms_tons():
    print()


def kilograms_grams():
    print()


def kilograms_tonnes():
    print()

# 6: conversion functions for tonnes : others


def tonnes_ounces():
    print()


def tonnes_pounds():
    print()


def tonnes_tons():
    print()


def tonnes_grams():
    print()


def tonnes_kilograms():
    print()


weight_menu = {
    1: {
        1: str_call,
        2: ounces_pounds,
        3: ounces_tons,
        4: ounces_grams,
        5: ounces_kilograms,
        6: ounces_tonnes
    },
    2: {
        1: pounds_ounces,
        2: str_call,
        3: pounds_tons,
        4: pounds_grams,
        5: pounds_kilograms,
        6: pounds_tonnes
    },
    3: {
        1: tons_ounces,
        2: tons_pounds,
        3: str_call,
        4: tons_grams,
        5: tons_kilograms,
        6: tons_tonnes
    },
    4: {
        1: grams_ounces,
        2: grams_pounds,
        3: grams_tons,
        4: str_call,
        5: grams_kilograms,
        6: grams_tonnes
    },
    5: {
        1: kilograms_ounces,
        2: kilograms_pounds,
        3: kilograms_tons,
        4: kilograms_grams,
        5: str_call,
        6: kilograms_tonnes
    },
    6: {
        1: tonnes_ounces,
        2: tonnes_pounds,
        3: tonnes_tons,
        4: tonnes_grams,
        5: tonnes_kilograms,
        6: str_call
    }
}
