#!/usr/bin/env python3
""" Alta3 Student Project | JStowe
    Temperature conversion Functions """


def fahrenheit_celsius(entry):
    """Fahrenheit to Celsius"""
    cels = (entry - 32) * (5 / 9)
    print(f"The temperature in Celsius is {cels:.2f} degrees.")
    # C = (F - 32) * (5/9)


def fahrenheit_kelvin(user_input):
    """Fahrenheit to Kelvin"""
    kelv = (user_input - 32) * (5 / 9) + 273.15
    print(f"The temperature in Kelvin is {kelv:.2f} degrees.")
    # K = (F - 32) * (5/9) + 273.15


def celsius_fahrenheit(user_input):
    """Celsius to Fahrenheit"""
    fahr = (user_input + 32) * (9 / 5)
    print(f"The temperature in Fahrenheit is {fahr:.2f} degrees.")
    # F = (F + 32) * (9 / 5)


def celsius_kelvin(user_input):
    """Celsius to Kelvin"""
    kelv = (user_input + 273.15)
    print(f"The temperature in Kelvin is {kelv:.2f} degrees.")
    # K = (C + 273.15)


def kelvin_fahrenheit(user_input):
    """Kelvin to Fahrenheit"""
    fahr = 1.8 * (user_input - 273) + 32
    print(f"The temperature in Fahrenheit is {fahr:.2f} degrees.")
    # F = 1.8 * (K - 273) + 32


def kelvin_celsius(user_input):
    """Kelvin to Celsius"""
    cels = (user_input - 273.15)
    print(f"The temperature in Celsius is {cels:.2f} degrees.")
    # C = (K - 273.15)
