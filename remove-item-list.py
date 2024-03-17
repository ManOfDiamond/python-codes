l = [1, 12, 1341, 204, 22]
print("List:", l)
a = int(input("Enter the element to be removed: "))  # Convert user input to integer
l1 = [i for i in l if i != a]  # Use list comprehension to create a new list without the element to be removed
print("Updated list:", l1)