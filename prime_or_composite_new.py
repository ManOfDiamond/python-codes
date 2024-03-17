#WAP to check if a number is prime or not
n = int(input("Enter a number: "))
l = n//2 + 1
e = 0
for i in range(2,l):
    if n % i == 0:
        e = 1
        break
if e == 1:
    print(n, "is a composite number.")
else:
    print(n, "is a prime number.")