#WAP to check if a word is palindrome or not
w = str(input("Enter a word: "))
if w == w[::-1]:
    print(w, "is a palindrome.")
else:
    print(w, "is not a palindrome.")
'''
Output:
Enter a number: 12345654321
12345654321 is a palindrome.
'''