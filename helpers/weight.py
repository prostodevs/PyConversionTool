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
    print(f"{user_input} ounces is {kilograms:.7f} kilograms")

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
    print(f"{user_input} pounds is {grams:.2f} grams")

def pounds_kilograms():
    user_input = try_catch()
    kilograms = user_input / (2.2046)
    print(f"{user_input} pounds is {kilograms:.4f} kilograms")

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
    print(f"{user_input} tons is {kilograms:.2f} kilograms")

def tons_tonnes():
    user_input = try_catch()
    tonnes = user_input / (1.1023)
    print(f"{user_input} tons is {tonnes:.2f} tonnes")


# 4: conversion functions for grams : others
def grams_ounces():
    user_input = try_catch()
    ounces = user_input * (0.035274)
    print(f"{user_input} grams is {ounces:.2f} ounces")

def grams_pounds():
    user_input = try_catch()
    pounds = user_input * (0.0022046)
    print(f"{user_input} grams is {pounds:.2f} pounds")

def grams_tons():
    user_input = try_catch()
    tons = user_input * (0.0000011023)
    print(f"{user_input} grams is {tons:.9f} tons")

def grams_kilograms():
    user_input = try_catch()
    kilograms = user_input / (1000)
    print(f"{user_input} grams is {kilograms:.7f} kilograms")

def grams_tonnes():
    user_input = try_catch()
    tonnes = user_input / (1000000)
    print(f"{user_input} grams is {tonnes:.9f} tonnes")


# 5: conversion functions for kilograms : others
def kilograms_ounces():
    user_input = try_catch()
    ounces = user_input * (35.274)
    print(f"{user_input} kilograms is {ounces:.2f} ounces")

def kilograms_pounds():
    user_input = try_catch()
    pounds = user_input * (2.2046)
    print(f"{user_input} kilograms is {pounds:.2f} pounds")

def kilograms_tons():
    user_input = try_catch()
    tons = user_input * (.0011023)
    print(f"{user_input} kilograms is {tons:.2f} tons")

def kilograms_grams():
    user_input = try_catch()
    grams = user_input / (0.001)
    print(f"{user_input} kilograms is {grams:.2f} grams")

def kilograms_tonnes():
    user_input = try_catch()
    tonnes = user_input / (1000)
    print(f"{user_input} kilograms is {tonnes:.4f} tonnes")

# 6: conversion functions for tonnes : others
def tonnes_ounces():
    user_input = try_catch()
    ounces = user_input * (35274)
    print(f"{user_input} tonnes is {ounces:.2f} ounces")

def tonnes_pounds():
    user_input = try_catch()
    pounds = user_input * (2204.6)
    print(f"{user_input} tonnes is {pounds:.2f} pounds")

def tonnes_tons():
    user_input = try_catch()
    tons = user_input * (1.1023)
    print(f"{user_input} tonnes is {tons:.2f} tons")

def tonnes_grams():
    user_input = try_catch()
    grams = user_input / (0.000001)
    print(f"{user_input} tonnes is {grams:.2f} grams")

def tonnes_kilograms():
    user_input = try_catch()
    kilograms = user_input / (0.001)
    print(f"{user_input} tonnes is {kilograms:.2f} kilograms")

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
