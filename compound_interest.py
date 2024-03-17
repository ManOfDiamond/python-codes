# WAP to for calculating compound interest
print("Compound Interest Calculator (yearly)")
p = int(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest per year (%): "))
n = float(input("Enter time period (years): "))
ci = p * ((1+r/100) ** n)
print("Compound Interest:", round(ci, 2))
'''
Output:
Compound Interest Calculator (yearly)
Enter the principal amount: 10000
Enter the rate of interest per year (%): 1.4
Enter time period (years): 2
Compound Interest: 10281.96
'''