#!python3
"""
Debug this program so that it runs

original code:
x = input("enter a decimal number"))
xi = int(x)
if (x - xi) == 0:
    print(f"{x} is an integer")
"""
x = float(input("enter a decimal number"))
xi = round(x)
if (x - xi) == 0:
    print(f"{x} is an integer")