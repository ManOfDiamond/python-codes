n = int(input("Enter a number: "))
f = 1
for i in range(1,n+1):
    f*=i
print("Factorial of {} is {}".format(n,f))