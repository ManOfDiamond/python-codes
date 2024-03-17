#WAP to print absolute value of a number entered by user
n = float(input("Enter a number: "))
if n >= 0:
    print("Absolute Value of", n, "is", n)
elif n < 0:
    print("Absolute Value of", n, "is", n*-1)
'''
Output:
Enter a number: -5
Absolute Value of -5.0 is 5.0
'''