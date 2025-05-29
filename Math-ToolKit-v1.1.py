# Math Toolkit 1.1 by Uzair_902
#https://www.youtube.com/@FixDroid-Pro
# A beginner-friendly command-line calculator with colorful output
#Sunday-May-25-2025-4:21PM
#START

import math
from colorama import init, Fore, Back, Style

init(autoreset=True)



#LABEL
label = 'Math ToolKit 1.1'.center(50)

print(Fore.YELLOW + Back.LIGHTRED_EX + Style.BRIGHT + label)




#DEFINING FUNCTIONS

#MENU FUNCTION
def show_menu():
    menu = """
Select an Operation:
Square Root   [sqrt]
Square        [sq]
Cube          [cb]
Cube Root     [cbrt]
Exponent      [exp]
LCM           [lcm]
Multiply      [mt]
Divide        [dv]
Sum           [sm]
Subtract      [sb]
Log           [log]
    """
    print(Fore.CYAN + Style.BRIGHT + menu)



# MATHS FUNCTIONS

#SQUARE ROOT
def squareroot():
	try:
		n = float(input('Enter Number:'))
		print(Fore.GREEN+ f'SQUARE ROOT: {n**(0.5)}')
	except Exception:
		print(Fore.LIGHTRED_EX+'\nERROR: Invalid Input')


#SQUARE OF A NUMBER
def square():
	try:
		n = float(input('Enter Number:'))
		print(Fore.GREEN+ f'SQUARE: {n**2}')
	except Exception:
		print(Fore.LIGHTRED_EX+'\nERROR: Invalid Input')


#CUBE OF A NUMBER
def cube():
	try:
		n = float(input('Enter Number:'))
		print(Fore.GREEN+ f'CUBE: {n**3}')
	except Exception:
		print(Fore.LIGHTRED_EX+'\nERROR: Invalid Input')


#CUBE ROOT 
def cuberoot():
	try:
		n = float(input('Enter Number:'))
		print(Fore.GREEN+ f'CUBE ROOT: {n**(1/3)}')
	except Exception:
		print(Fore.LIGHTRED_EX+'\nERROR: Invalid Input')


#CUSTOM EXPONENT 
def exponent():
	try:
		n = float(input('Enter Number:'))
		exp = int(input('Enter Exponent:'))
		print(Fore.GREEN+ f'RESULT: {n**exp}')
	except Exception:
		print(Fore.LIGHTRED_EX+'\nERROR: Invalid Input')


# LCM
def lcm():
	try:
		n = input('Enter Number, Use Commas to seperate multiple values:')
		n = n.split(',')
		n = list(map(float, n))
		print(Fore.GREEN+ f'LCM: {math.lcm(*n)}')
	except Exception:
		print(Fore.LIGHTRED_EX+'\nERROR: Invalid Input')


# MULTIPLICATION
def multiply():
	try:
		n = input('Enter Number, Use Commas to seperate multiple values:')
		n = n.split(',')
		n = list(map(float, n))
		print(Fore.GREEN+ f'PRODUCT: { math.prod(n)}')
	except Exception:
		print(Fore.LIGHTRED_EX+'\nERROR: Invalid Input')


# DIVISION
def divide():
	try:
		n = float(input('Enter Dividend Number:'))
		n2 = float(input('Enter Divisor Number:'))

		print(Fore.GREEN+ f'DIVSION: {n/n2}')
	except Exception as e:
		print(Fore.LIGHTRED_EX+f'\nERROR: {e}')


# ADD
def add():
	try:
		n = input('Enter Number, Use Commas to seperate multiple values:')
		n = n.split(',')
		n = list(map(float, n))
		print(Fore.GREEN+ f'SUM: {sum(n)}')
	except Exception:
		print(Fore.LIGHTRED_EX+'\nERROR: Invalid Input')


# SUBTRACT
def subtract():
	try:
		n = float(input('Enter 1st Number:'))
		n2 = float(input('Enter 2nd Number: '))

		print(Fore.GREEN+ f'SUBTRACT: {n-n2}')
	except Exception:
		print(Fore.LIGHTRED_EX+'\nERROR: Invalid Input')


# LOG BASE 10
def log():
	try:
		n = float(input('Enter Number:'))
		print(Fore.GREEN+ f'LOG: {math.log10(n)}')
	except Exception:
		print(Fore.LIGHTRED_EX+'\nERROR: Invalid Input')


# MAIN FUNCTION
def main():
	ip = input(Fore.YELLOW+'\nEnter an Option: ')
	if ip.lower() == 'sqrt':
		squareroot()
	elif ip.lower() == 'sq':
		square()
	elif ip.lower() == 'cb':
		cube()
	elif ip.lower() == 'cbrt':
		cuberoot()
	elif ip.lower() == 'exp':
		exponent()
	elif ip.lower() == 'lcm':
		lcm()
	elif ip.lower() == 'mt':
		multiply()
	elif ip.lower() == 'dv':
		divide()
	elif ip.lower() == 'sm':
		add()
	elif ip.lower() == 'sb':
		subtract()
	elif ip.lower() == 'log':
		log()
	elif ip.lower() == '':
		print(Fore.RED + Style.BRIGHT + '\nERROR: INVALID INPUT')
	else:
		print(Fore.RED + Style.BRIGHT + '\nERROR: INVALID INPUT')

show_menu()
while True:
	try:
		main()
	except Exception as e:
		print(Fore.RED+ f'\nAN ERROR ({e}) OCCURED. PLEASE MAKE SURE YOUR INPUT IS VALID.')
		break