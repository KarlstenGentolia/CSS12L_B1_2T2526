###1.) Ask for first name, middle name, and last name. Format the output as: Last Name, First Name M.with proper capitalization)###

def name():
	x = input("Enter your first name: ")
	y = input("Enter your middle name: ")
	z = input("Enter your last name: ")

	first = x.lower().title().strip()
	middle = y.lower().capitalize()[0]
	last = z.lower().capitalize().strip()

	print(f"Your formated name is: {last}, {first} {middle}.")
 
name()

###2.) Ask for a word and an integer N. Print the word in a growing pyramid pattern up to N times.###

def pyramid():
	word = input("Enter a word: ")
	number = int(input("Enter a number: "))

	for w in range(1, number + 1):
		print(word*w)

pyramid()

###3.) Ask for a sentence and return the total characters, words, and vowels###
def length():
	z = input("Enter sentence: ")
	sentence = z.title().strip()
	word_list = sentence.split()
	a = len(word_list)
	b = len(sentence)

	def vowels(text):
		bilang = 0
		vowels = "aeiouAEIOU"
		for c in text:
			if c in vowels:
				bilang += 1
		return bilang

	total_vowels = vowels(sentence)	

	print(f"""Characters: {b}
Words: {a}
Vowels: {total_vowels}""")		

length()

###4.) Ask for a word and check if it's a palindrome (same forward and backward)###
def palindrome():
	w = input("Enter a word: ")
	word = w.lower()
	reverse = word[::-1]

	if reverse == word:
		print("This word is a Palindrome")
	else:
		print("This word is not a  Palindrome")	

palindrome()

###5.) Ask for a phrase and display it in uppercase and reversed.###
def shout():
	x = input("Enter a Phrase: ")
	shout = x.upper()

	print(shout[::-1])

shout()

###6.) Ask the user to input an email address and check validity(with errors and such)###
def email():
	email = input("Enter your email: ")

	index = email.find("@")

	if (email.count("@")==1) and (email.count(".")!=0):
		user = email[:index]
		username = user.lower()
		format_user = username.replace(".", " ").replace("_", " ")

		print(f"Your username is {format_user}")
	else:
		print("Invalid email! Must Contain @ and .")	

email()

###7.) Ask the user to input an email address and check advanced validity.###
def gmail():
	email = input("Enter your email: ")

	index = email.find("@")

	if (email.count('@')==0):
		print("Invalid email! Must Contain @")
	elif " " in email:
		print("Invalid Email! Must not contain space!")
	elif (email.count("@")!=1):
		print("Invalid Email! Must not contain more than one @ symbol!")
	elif not email.endswith(".com") or email.endswith(".edu") or email.endswith(".org"):
		print("Invalid Email! Must with .com, .org, or .edu")
	else:
		user = email[:index]
		domain = email[index + 1:]

		username = user.lower().replace("_", " ").replace(".", " ")

		print(f"""Your username is {user}
Your domain is {domain}""")
gmail()