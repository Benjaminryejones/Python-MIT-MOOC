from decimal import Decimal
import sys

sys.setrecursionlimit(10000)

def creditCardQuestion1():
	balance = float(raw_input('Please enter your outstanding balance'))
	interestRate = float(raw_input('Please enter your annual interest rate'))
	monthyPaymentRate = float(raw_input('Please enter your monthly payment rate'))
	numMonths = float(raw_input('Please enter the number of months to calculate'))

	creditCardBalance(balance, interestRate, monthyPaymentRate, numMonths)

def minimumMonthly(monthly_rate, balance):
	"""Enter the monthly payment rate and current balance"""
	return round(Decimal(monthly_rate * balance, 4))

def interestPaid(annual_rate, balance):
	"""Enter the annual rate and current balance"""
	return round(Decimal((annual_rate / 12) * balance, 4))

def principlePaid(monthly_rate, interestPaid):
	"""Enter the monthly rate and the result of the interestPaid function"""
	return round(Decimal(monthly_rate - interestPaid, 4))

def remainingBalance(balance, principlePaid):
	"""Enter the balance and the results of the principlePaid function"""
	return round(Decimal(balance - principlePaid, 4))

def creditCardBalance(balance, interestRate, monthyPaymentRate, numMonths):
	if numMonths == 0:
		return "No months remain"
	else:
		minMonth = minimumMonthly(monthyPaymentRate, balance)
		intPaid = interestPaid(interestRate, balance)
		pinPaid = principlePaid(monthyPaymentRate, intPaid)
		remBalance = remainingBalance(balance, pinPaid)
		print "Month %d:" % numMonths
		print "Minimum Payment: \t$%.2f" % minMonth
		print "Interest Paid: \t$%.2f" % intPaid
		print "remainingBalance: \t$%.2f" % remBalance

		return creditCardBalance(balance - pinPaid, interestRate, monthyPaymentRate, numMonths-1)

def creditCardQuestion2():
	print "This program allows you to calculate the minimum monthly payments required to pay off your debt in 12 months or less."
	balance = float(raw_input('Please enter your outstanding balance'))
	interestRate = float(raw_input('Please enter your annual interest rate'))

	creditCardPaymentsYear(balance, interestRate)

def creditCardPaymentsYear(balance, interestRate):
	monthly_rate = interestRate / 12
	numMonths = 0
	minimumMonthly = 10
	global balanceTest
	balanceTest = balance


	creditPaymentTester(balance, interestRate, monthly_rate, minimumMonthly, numMonths)

def creditPaymentTester(balance, interestRate, monthly_rate, minimumMonthly, numMonths):
	new_balance = balance
	if new_balance <= 0 and numMonths < 13:
		print "Monthly payment amount to pay off debt in one year: %.2f" % minimumMonthly
		print "Number of months needed: %d" % numMonths
		print "Balance: %.2f" % balance
	elif numMonths > 13:
		return creditPaymentTester(balanceTest, interestRate, monthly_rate, minimumMonthly + 10, 0)
	else:
		new_balance = new_balance * (1 + monthly_rate) - minimumMonthly
		numMonths += 1
		return creditPaymentTester(new_balance, interestRate, monthly_rate, minimumMonthly, numMonths)

def creditCardQuestion3():
	print "This program allows you to calculate the minimum monthly payments required to pay off your debt in 12 months or less using bisectional search."
	balance = float(raw_input('Please enter your outstanding balance'))
	interestRate = float(raw_input('Please enter your annual interest rate'))
	monthly_rate = interestRate / 12

	# Bisection values
	lower = balance / 12
	upper = (balance * ((1 + monthly_rate) ** 12)) / 12
	tolerance = .01

	bisectionalSearch(balance, interestRate, lower, upper, tolerance)


def bisectionalSearch(balance, interestRate, lower, upper, tolerance):

	origBalance = balance
	monthly_rate = interestRate / 12

	while (balance >= tolerance):

		guess = (upper + lower) / 2

		for month in range (1, 13):
			balance -= guess
			balance += balance * monthly_rate

		if balance > tolerance and balance > 0:
			lower = guess
			balance = origBalance
		elif balance < 0 and balance > -tolerance:
			upper = guess
			balance = origBalance
		else:
			print "Monthly payment amount to pay off debt in one year: %.2f" % guess
			break











creditCardQuestion1()
creditCardQuestion2()
creditCardQuestion3()

