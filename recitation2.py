#While loop example
even_number = 2
while (even_number <= 10):
	print even_number
	even_number += 2

#For loop example
for i in (2, 4, 6, 8, 10): #Tuple literal
	print i

#The range function
#Range parameters: inclusive, exclusive, step. Expects integers -- it will truncate floats.
print range(100)

#Can type help(function) to get documentation help. Square brackets indicate optional parameters.

for i in range (2,11,2):
	print i

#Tuple -- is a non-scalar data type that can hold many items. Scalar: can only hold one element at a time.
tuple_of_numbers = (1, 100, -100, 55)

#Tuples start at index 0
print tuple_of_numbers[1]
print tuple_of_numbers[-1] #Go to the end and walk back [] steps

#Number of elements in the tuple
print len(tuple_of_numbers)

#Mixed data type tuple
tuple_mixed = (1, 100, 'hello', 'dix')

#Can also nest tuples

#Tuples are immuatable (can't change data after it has been assigned)

#Tuple slicing
tuple_of_numbers[0:3] #Elements one and two -- because the range is exlusive
tuple_of_numbers[:2] #Implicit start and end
tuple_of_numbers[1:]
tuple_of_numbers[:] #Slice the entire tuple_of_numbers
tuple_of_numbers[:-1] #0 to the last element

#Can for loop tuples
#for number in tuple_of_numbers
#	print number

tuple_of_numbers = tuple_of_numbers + (1, 100) #Can "append" to tuples. You're actually creating a new tuple

#Wart
#Parenthesis share a dual purpose -- to make a tuple out of a lone element, you need to add a comma
oopsie = (50) #Not a tuple
oopsie = (50,) #This is correct

#############################
#Strings -- a lot like tuples

name = 'Mitch'

print name
print name[2] #Prints t

for letter in name:
	print letter #prints it, seemingly vertically

#Can also slice Strings
name[1:3]

#String functions
print name.upper()
print name.lower()
print name.find('i') #Returns -1 if string not found
name = name.replace('M','P', 1) #Sensative to caps

#dir(str) returns possible commands/functions


############################
#Break kicks you out of a loop -- the innermost loop
for i in range(0, 10):
	for j in range(10, 100):
		print i, j
		if j % 2 == 0:
			break


###########################
#Functions -- extremely important. A bit of code that is named and takes input, does something with it, and returns a value
#""" <- doc string, describes the function. Best to specify inputs and outputs.

all_hope = "Here be dragons"
def var_stealer(variables):
	"""Steals all your variables.
	Input: variables
	Output: None (stolen)
	"""

##########################
#Print =/= return