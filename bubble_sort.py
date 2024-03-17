#bubble sort
l = []
n = int(input("Enter the no. of elements to be added: "))
'''for i in range(n):
    e = eval(input("Enter element {}: ".format(i+1)))
    l.append(e)
'''
l = [eval(input("Enter element {}: ".format(i+1))) for i in range(n)]
print(l)
for i in range(1,len(l)):
    for j in range(i,0,-1):
        if l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
    print("Step {} : {}".format(i,l))