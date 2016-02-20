first_number = raw_input("Please enter in a number: ")

second_number = raw_input("Please enter in a number number: ") 
try:
	if int(first_number) > int(second_number):
		print "The first number {} is greater than the second number {}.".format(first_number, second_number)
	elif int(first_number) < int(second_number):
		print "The first number {} is less than the second number {}".format(first_number, second_number)
	elif int(first_number) == int(second_number):
		print "The first number {} is equal to the second number {}".format(first_number, second_number)
except:
	print "Please type in numbers!"