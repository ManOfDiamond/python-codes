#WAP to check if a string is palindrome or not
s = str(input("Enter a string: "))
if s == s[::-1]:
    print(s, "is a palindrome.")
else:
    print(s, "is not a palindrome.")
'''    
Output:
Enter a string: hello world
hello world is not a palindrome.
'''