l,l1 = [1,12,1341,204,22], []
print("List:",l)
a = int(input("Enter the element to be removed: "))  # Convert user input to integer
for i in l:
    if i != a:
        l1.append(i)
print("Updated list:",l1)