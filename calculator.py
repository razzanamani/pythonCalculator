#!usr/bin/python
#Interpreter: Python3
#Program to create a functioning calculator

def welcome():
	print('Welcome to the Calculator.')


def again():
	again_input = input('''
	Do you want to calculate again?
Press Y for YES and N for NO
''')

	# if user types Y, run the calculate() function
	if again_input == 'Y':
		calculate()

	#if user types N, say bye
	elif again_input == 'N':
		print('Thank You for using Calculator')

	#if user types another key, run the same funtion again
	else:
		again()


def calculate():
	operation = input('''
	Please type the math operation you would like to complete:
+ for addition
- for substraction
* for multiplication
/ for division
''')

	number_1 = int(input('Enter the first number :'))
	number_2 = int(input('Enter the second number :'))

	#Addition
	if operation == '+':
		print('{} + {} = '.format(number_1,number_2))
		print(number_1 + number_2)

	#Substraction
	elif operation == '-':
		print('{} - {} = '.format(number_1,number_2))
		print(number_1 - number_2)

	#Multiplication
	elif operation == '*':
		print('{} * {} ='.format(number_1,number_2))
		print(number_1 * number_2)

	#Division
	elif operation == '/':
		print('{} / {} = '.format(number_1,number_2))
		print(number_1/number_2)

	#else operation
	else:
		print('You have not typed a valid operator,please run the program again.')
	
	#calling the again() function to repeat 
	again()

#calling the welcome funtion
welcome()
#calling the calculator function outside the function
calculate()


