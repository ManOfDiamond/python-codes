# Simple Calculator
while True:
	# take input from the user
	choice = input('''What do you want to do?
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice(1/2/3/4): ''')

	# check if choice is one of the four options
	if choice in ('1', '2', '3', '4'):
		n1 = float(input("Enter first number: "))
		n2 = float(input("Enter second number: "))
	a = n1 + n2
	s = n1 - n2
	d = n1 / n2
	m = n1 * n2
	p = n1 ** n2

	if choice == '1':
		print("Sum of {0} and {1} is {2}".format(n1,n2,a))

	elif choice == '2':
		print("Difference of {0} and {1} is {2}".format(n1,n2,s))

	elif choice == '3':
		print("Product of {0} and {1} is {2}".format(n1,n2,m))

	elif choice == '4':
		print("Division of {0} by {1} yields quotient = {2}".format(n1,n2,d))

	else:
		print("Invalid input, retrying") #if the value isn't one of the four options
		continue
	# check if user wants another calculation
	while True:
		ano = input("Another calculation?(y/N)")
		if ano == 'y':
			break
		elif ano == 'Y':
			break
		elif ano == 'n':
			exit("Thank you!")
		else:
			exit("Thank you!")
