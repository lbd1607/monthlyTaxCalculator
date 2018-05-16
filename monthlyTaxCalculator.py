#Laura Davis
#15 February 2016
#This program calculates and displays sales taxes based on monthly sales.
#The user will input the total month's sales and the program 
#will calculate county tax, state tax, and total tax.
#The total is county tax plus state tax. 

#This is the main function.
def main(): 
	print "Welcome to the sales tax calculator program."
	print #prints a blank line
	monthlySales = input_data()
	countyTax = calc_county(monthlySales)
	stateTax = calc_state(monthlySales)
	totalTax = calc_total(countyTax, stateTax)
	print_data(countyTax, stateTax, totalTax)
	
#This function will input the monthly sales.
def input_data():
	monthlySales = input("Enter the total monthly sales $")
	monthlySales = float(monthlySales)
	return monthlySales

#This function will calculate the county tax at 2%.
def calc_county(monthlySales):
	countyTax = monthlySales * .02
	return countyTax

#This function will calculate the state tax at 4%.
def calc_state(monthlySales):
	stateTax = monthlySales * .04
	return stateTax

#This function will calculate the total tax.
def calc_total(countyTax, stateTax):
	totalTax = countyTax + stateTax
	return totalTax

#This function will print the county tax, state tax, and total tax. 
def print_data(countyTax, stateTax, totalTax):
	print "The county tax is $", countyTax
	print "The state tax is $", stateTax
	print "The total tax is $", totalTax

#calls main
main()
