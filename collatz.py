'''
Simple program that determines the Collatz sequence for a user inputted number
Author: Sammy Tbeile
July 8 2017
'''
import sys
def collatz(number):
	if number % 2 == 0:
		number = number // 2
	else:
		number = 3 * number + 1
	print(number)
	return number

def error():
	print("Please input a positive integer")
	sys.exit()

guess = 0
try:
	guess = int(input("Enter a number: "))
except ValueError:
	error()

if(guess < 1):
	error()

while(guess != 1):
	guess = collatz(guess)
