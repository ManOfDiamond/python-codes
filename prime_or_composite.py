# WAP to find if a number is prime or composite
p = 0
n = int(input("Enter a number: "))
if n == 0 or n == 1:
    k = 1
for i in range(2,n):
    if n%i == 0:
        k = 1
    else:
        k = 0
if k == 1:
    print(n,"is a prime number.")
else:
    print(n,"is a composite number.")
'''
Output:
Enter a number: 538579
538579 is a composite number.
'''