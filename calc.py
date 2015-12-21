#================================================#
#== A very simple calculator written in Python ==#
#=             Made by RhozzDev                 =#
#=         p.s.: i am still a newbie.           =#
#=        p.s. 2: sorry for my english.         =#
#==          p.s. 3: I Love Python!!           ==#
#================================================#

#This imports a library to get the date time, i put this only to make the script looks better.
from datetime import datetime

#now will be the main variable to use for date time variables.
now = datetime.now()
#This will select the current hour, minutes, seconds, day, month and year.
hours = now.hour
minutes = now.minute
seconds = now.second
day = now.day
month = now.month
year = now.year

#This will print the current hour:minute:second - day/month/year
print "\nCurrent time: %d:%d:%d - %d/%d/%d" % (hours, minutes, seconds, day, month, year) + "\n"

#This is a list of valid operators for the calculator. remove the """ in the begin and the end of this (if you want to see the list on the CONSOLE\TERMINAL)
"""print "A list of valid operators: + for add, - for substract, * for multiply, / for divide, ** for potenciation\n"
print "example of add: 1 + 1 = 2" + "\n"
print "example of substract: 2 - 1 = 1" + "\n"
print "example of multiply: 5 * 3 = 15" + "\n"
print "example of divide: 10 / 2 = 5" + "\n"
print "example of potenciacion: 5 ** 2 = 25" + "\n" """

#Here the user will define the variable number1, the operator and the number2 as STRINGs.
number1 = raw_input("First Number: ")
operator = raw_input("operator: ")
number2 = raw_input("Second Number: ")

#But here we change the STRING of number1 and number2 to INTEGERs.
num1 = int(number1)
num2 = int(number2)

#As you can see above, the if sentence will check what operator was typed, and this functions will do what the typed operator is for.

#This function will ADD the numbers between each one, and return the result.
def suma(arg1, arg2):
	return arg1 + arg2

#This function will SUBSTRACT the numbers between each one, and return the result.
def resta(arg1, arg2):
	return arg1 - arg2

#This function will DIVIDE the numbers between each one,and return the result.
def div(arg1, arg2):
	return arg1 / arg2

#This function will MULTIPLY the numbers between each one, and return the result.
def mult(arg1, arg2):
	return arg1 * arg2

#This function will POTENCY the numbers between each one, and return the result.
def pot(arg1, arg2):
	return arg1 ** arg2

#the "if" operator will check what operator has typed, if none, or another that isn't in this list, will return the 'else' print.
#the str() will make the result "int" to a "string", because STRINGS and INTs cannot be concatenated.
if operator == "+":
	print "\nResult: " + str(suma(num1, num2)) + "\n"
elif operator == "-":
	print "\nResult: " + str(resta(num1, num2)) + "\n"
elif operator == "%" or operator == "/":
	print "\nResult: " + str(div(num1, num2)) + "\n"
elif operator == "*" or operator == "x" or operator == ".":
	print "\nResult: " + str(mult(num1, num2)) + "\n"
elif operator == "**":
	print "\nResult: " + str(pot(num1, num2)) + "\n"
else:
	print "\nSorry, but the operator is not recognized, please try again."

#End of Script z3 (z3 means a styled heart)
