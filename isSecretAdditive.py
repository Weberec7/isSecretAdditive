#!/usr/bin/python
import argparse


def isPrime( number ):
	"Determines if the given number is Prime"
	#No number greater than half of the original number will be
	# a divisor.  Do not include this half in testing range.
	for num in range (2, number/2 + 1):
		if number%num == 0:
			return False
	return True

def findPrimesLessThan( number ):
	"Finds a list of all prime numbers less than the given number"
	myList = []
	for num in range( 2, number ):
		if isPrime(num):
			myList.append( num )
	return myList	

def secret( numberIn ):
	"A secret function that takes a number and returns a number"
	numberOut = numberIn/3
	return numberOut

def isSecretAdditive( primeList ):
	"Tests is secret() additive across all combinations of integers from a given list"
	for num1 in primeList:
		for num2 in primeList:
			if num1 == num2:
				#Don't include combinations of the same prime number
				continue
			if secret(num1 + num2) != secret(num1) + secret(num2):
				return False

	return True

def main():
	#set limit since Prime Number checks are cpu intensive
	userNumberLimit = 150000

	parser=argparse.ArgumentParser(
		description='''Accepts a single integer parameter and returns an integer.  Determines if the number is additive [secret(x+y) = secret(x) + secret(y)], for all combinations x and y, where x and y are all prime numbers less than the number passed via the command-line argument. The function secret() accepts an integer and returns an integer.''',
		epilog="""Made By Ethan Weber, Enjoy!""")
	parser.add_argument('userNumber', type=int, default=0, help="#choose a positive integer")


	#Include extra options to easily expose functions in the script.
	parser.add_argument('-ip', action='store_true', help='test if userNumber prime?')
	parser.add_argument('-ap', action='store_true', help='show all primes less than userNumber')
	parser.add_argument('-r', action='store_true', help='test isSecretAdditive for all numbers less than userNumber')
	parser.add_argument('-nl', action='store_true', help='remove upper limit on userNumber')
	args=parser.parse_args()


	#Throw error if userNumber > userNumberLimit
	if args.userNumber > userNumberLimit and not args.nl:
		parser.error("input Number above suggested limit.  use -rl to remove limit.")

	# As is only one option will execute at a time.
	if args.ip:
		print isPrime(args.userNumber)
	elif args.ap:
		print findPrimesLessThan(args.userNumber)
	elif args.r:
		for num in range( 1, args.userNumber ):
			print isSecretAdditive(findPrimesLessThan(num)), num

	#Default to core functionality.
	else:
		print isSecretAdditive(findPrimesLessThan(args.userNumber))


if __name__ == "__main__":
	main()
	exit()


