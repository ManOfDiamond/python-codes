#WAP to to print first 10 natural numbers in reverse order and find their sum
s = 0
for i in range(10,0,-1):
    print(i)
    s = s + i
print("Sum of first 10 natural numbers is:",s)
'''
Output:
10
9
8
7
6
5
4
3
2
1
Sum of first 10 natural numbers is: 55
'''