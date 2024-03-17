#WAP to print the fibonacci series 0, 1, 1, 2, 3, 5, 8........
n = int(input("Enter number of elements: "))
a, b = 0, 1
print(a,b,end=' ')
for i in range(0,n-2):
    c = a + b
    print(c,end=" ")
    a, b = b, c