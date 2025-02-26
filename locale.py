import sys
import re
import os

cl_input = sys.argv[0:]

#If the input length is 1, i.e. only the script name, it throws an error to enter arguments.
if len(cl_input) == 1:
    print("Please enter arguments. e.g. python locale.py [option] [argument_file]")
    sys.exit(1)
else:
    input = sys.argv[1:] #Input takes all command line arguments from second argument [1] onwards e.g. option language argument_file.
    option = input[0] #option is always the first after the script name.
    argument_file = input[-1] #argument_file is always the last in the list.

#If the option is -l, the expected length of input is 3 (1.option 2.language 3.argument_file).
if option == "-l": 
	if len(input) == 3:
		language = input[1]
	else: #If the length isn't 3, throws a format error.
		print("Please enter a valid argument format. e.g. python locale.py -l [language] [argument_file]")
		sys.exit(1)

#If the option is anything else, the expected length of input is 2 (1.option 2.argument_file). It throws are error if the format is incorrect.
else: 
	if not len(input) == 2:
		print("Please enter a valid argument format. e.g. python locale.py [option] [argument_file]")
		sys.exit(1)

#The below checks if the argument file exists and is readable, produces an error and exits if not.
if os.access(argument_file, os.R_OK):
	read = open(argument_file, "r")
else:
	print("Error reading or accessing the argument file")
	sys.exit(1)

#The below creates a new list and appends it with the stripped and split content of the read file.
info = []
for line in read:
	line = line.strip('\n').split(',')
	info.append(line)

#The below is a function for the -a option which prints the filenames of all the available locales in appearance order.
def a_option(info):
	locale_exist = False
	for line in info:
		if line[0] == 'locale':
			locale_exist = True
			print("Available locales:")
			for line in info:
				if line[0] == "locale":
					print(line[2])
				else:
					continue
			break
	if not locale_exist:
		print("No locales available")

#The below is a function for the -m option which prints the filenames of all available charmaps in appearance order.
def m_option(info):
	charmap_exist = False
	for line in info:
		if line[0] == 'charmap':
			charmap_exist = True
			print("Available charmaps:")
			for line in info:
				if line[0] == "charmap":
					print(line[2])
				else:
					continue
			break
	if not charmap_exist:
		print("No charmaps available")

#The below is a function for the -l option which searches for the language input, and prints the total number of locales and charmaps for that language.
def l_option(info,language):

	language_count = {}
	locale_count = 0
	charmap_count = 0
	language_exist = False

	for line in info:
		#The below throws an error if the argument file is empty or without sufficient content.
		try:
			file_language = line[1].lower() #I have added .lower() to convert the string to a consistent format for a better search. Can be removed if high input specificity is desired.
		except:
			print("Error finding language in the argument file")
			sys.exit(1)

		if file_language == language.lower():
			language_exist = True
			if line[0] == 'locale': 
				locale_count += 1
			elif line[0] == 'charmap':
				charmap_count += 1
			else:
				language_count[language] = 1
	
	if not language_exist:
		print("No locales or charmaps in this language")
		exit()

	language = language.capitalize() #Capitalises the first character of the string to align with the format in the assignment document. e.g. 'Language English'.
	print("Language " + str(language) + ":")
	print("Total number of locales:",locale_count)
	print("Total number of charmaps:",charmap_count)

#The below is a function for the -v option which prints my name, surname, student ID and completion date for this assignment in my chosen format.
def v_option(info):
	print("First Name: Kyle")
	print("Last Name: McKinstry")
	print("Student ID: 24549952")
	print("Completion Date: 15/05/2024")

#The below calls a function depending on the input option and throws an error if the option is unavailable then providing a list of accepted options.
if option == '-a':
	a_option(info)
elif option == '-m':
	m_option(info)
elif option == '-l':
	l_option(info,language)
elif option == '-v':
	v_option(info)
else: 
	print("Invalid option. Accepted options include: \n(-a): Available locales\n(-m): Available charmaps\n(-l): Total locales and charmaps for a provided language\n(-v): Student information")
	sys.exit(1)