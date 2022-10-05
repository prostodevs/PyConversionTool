#!/usr/bin/env python3

def fahrenheit_celsius(int):
    cels = (int - 32) * (5/9)
    print(f"The temperature in Celsius is {cels}")


def fahrenheit_kelvin(int):
    fahr = int(input("What is the temperature in fahrenheit?\nEnter: "))
    kelv = (int - 32) * (5/9) + 273.15
