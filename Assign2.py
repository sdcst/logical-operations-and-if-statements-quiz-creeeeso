"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

x=float(input("Enter a number: "))
y=float(input("Enter a number: "))
z=str(input(f'Is one of the number the hypotense of a right triangle? \nIf the answer is yes answer "Yes": '))
while z!= "Yes":
    x=float(input("Enter a number: "))
    y=float(input("Enter a number: "))
    z=str(input(f'Is one of the number the hypotense of a right triangle? \nIf the answer is yes answer "Yes": '))
else:
    a=min(x,y)
    c=max(x,y)
    b=((x**2)-(y**2))**0.5
    b=round(b,1)
    print(f"The length of the missing side is {b}") 
      






