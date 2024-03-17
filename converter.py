# WAP to input a number in decimal and convert it to binary, octal, hexadecimal
print("Number System Converter")
print("""What do you want to do?
      1. Convert Decimal to Binary
      2. Convert Decimal to Octal
      3. Convert Decimal to Hexadecimal""")
while True:
    a = input("Enter your choice(1/2/3): ")
    if a in ('1','2','3'):
        b = int(input("Enter your decimal number here: "))
        if a == '1':
            print(b, 'in binary is', bin(b) [2: ])
            exit("Thanks!")
        elif a == '2':
            print(b, 'in octal is', oct(b) [2: ])
            exit("Thanks!")
        else:
            print(b, 'in hexadecimal is', hex(b) [2: ])
            exit('Thanks!')
    else:
        print("Invalid input, retrying")
        continue
'''
Output:
Number System Converter
What do you want to do?
      1. Convert Decimal to Binary
      2. Convert Decimal to Octal
      3. Convert Decimal to Hexadecimal
Enter your choice(1/2/3): 2
Enter your decimal number here: 225
225 in octal is 341
Thanks!
'''