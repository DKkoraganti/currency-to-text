# Python program to convert currency into text form

'''  Write a console application in the choice of your programming language that takes in a currency value 
(Min Value 00, Max Value 9,99,999.99) and prints out a text. For ex. 
If provided "123456.78", it should print out "Rs. One Lakh Twenty Three Thousand Four Hundred And Fifty Six 78/100 ONLY". 
'''



import re

list1 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

list2 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eigthy", "Ninty"]


# Checks whether the user input is of valid form or not
def validation(n):
	valid = False
	if re.match("^[0-9]{1,6}\.[0-9]{1,2}$", n) != None or re.match("^[0-9]{1,6}$", n) != None:
		valid = True
	else:
		valid = False
	return valid

# function to covert select numbers into text
def words(number):
	if number > 19:
		return list2[(number // 10) - 2] + ((" " + list1[(number % 10) - 1]) if (number % 10) > 0 else "")
	else:
		return list1[number - 1]

# function converts currency into text
def currencyText(n):
	output = "Rs. "
	
	# if input is valid, program proceeds, else it raises exception
	valid = validation(n)
	if valid == True:

		whole = int(float(n))
		fractional = round(float(n) - whole, 2)


		if float(n) == 0:
			output += "Zero "

		if whole // 100000 != 0 :
			output += words(whole // 100000) + " Lakh "
			whole = whole % 100000

		if whole // 1000 != 0 :
			output += words(whole // 1000) + " Thousand "
			whole = whole % 1000

		if whole // 100 != 0 :
			output += words(whole // 100) + " Hundred "
			whole = whole % 100
			if whole != 0:
				output += "And "

		if whole != 0 :
			output += words(whole) + " "

		if fractional != 0 :
			fractional *= 100
			output += str(int(fractional)) + "/100" + " "

		output += "ONLY"

		return output

	else:
		raise Exception("Invalid input, please match the currency pattern")

 
currency = input("Enter currency to be converted into text. (Ex. 123456.78) : ")
print(currencyText(currency))

