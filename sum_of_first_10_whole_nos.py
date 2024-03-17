#WAP to print first 10 whole numbers in reverse order and find their sum
s = 0
for i in range(10,-1,-1):
    print(i)
    s = s + i
print("Sum of first 10 whole numbers is:",s)
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
0
Sum of first 10 whole numbers is: 55
'''