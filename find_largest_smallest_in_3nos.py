#WAP to find the largest and smallest of three numbers
n1,n2,n3 = float(input("Enter a number: ")), float(input("Enter another number: ")), float(input("Enter another number: "))
if n1 > n2:
    if n2 > n3:
        print(n1, "is the largest number and", n3, "is the smallest number.")
    else:
        print(n1, "is the largest number and", n2, "is the smallest number.")
elif n2 > n3:
    if n3 > n1:
        print(n2, "is the largest number and", n1, "is the smallest number.")
    else:
        print(n2, "is the largest number and", n3, "is the smallest number.")
elif n3 > n1:
    if n1 > n2:
        print(n3, "is the largest number and", n2, "is the smallest number.")
    else:
        print(n3, "is the largest number and", n1, "is the smallest number.")
'''
Output:
Enter a number: 42.12479171719
Enter another number: 1249.113201
Enter another number: 10238.325539
10238.325539 is the largest number and 42.12479171719 is the smallest number.
'''