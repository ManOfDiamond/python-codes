s = str(input("Enter a string: "))
l = list(s)
n = int(input("Enter the index element you want to be replaced: "))
a = str(input("Enter string to replace it with: "))
l[n] = a
for i in l:
    print(i,end='')