#1

first_name = input("Enter your first name: ").strip()
middle_name = input("Enter your middle name: ").strip()
last_name = input("Enter your last name: ").strip()

first_formatted = first_name.capitalize()
last_formatted = last_name.capitalize()
middle_initial = middle_name[0].upper()

print(f"\nFormatted Name: {last_formatted}, {first_formatted} {middle_initial}.")

#2-------------------------------------------------------------------------------------------------------------------------------------------

word = input("Enter a word: ")
n = int(input("Enter a number: "))

print("\nOutput:")

for i in range(1, n + 1):
    print(word * i)


#3-------------------------------------------------------------------------------------------------------------------------------------------

sentence = input("Enter a sentence: ")

char_count = len(sentence)
word_count = len(sentence.split())

vowels = "aeiouAEIOU"
vowel_count = 0
for char in sentence:
    if char in vowels:
        vowel_count += 1

print(f"\nCharacters: {char_count}")
print(f"Words: {word_count}")
print(f"Vowels: {vowel_count}")

#4-------------------------------------------------------------------------------------------------------------------------------------------

word = input("Enter a word: ")

if word == word[::-1]:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")

#5-------------------------------------------------------------------------------------------------------------------------------------------


phrase = input("Enter a phrase: ")
shouted_backwards = phrase.upper()[::-1]
print(f"Output: {shouted_backwards}")

#6-------------------------------------------------------------------------------------------------------------------------------------------


email = input("Enter your email address: ")

if "@" in email and "." in email:
    at_index = email.find("@")
    username = email[:at_index]
    
    formatted_username = username.lower().replace(".", " ").replace("_", " ")
    
    print(f"Your username is: {formatted_username}")
else:
    print('Invalid email address. Please include "@" and a dot (.)')

#7-------------------------------------------------------------------------------------------------------------------------------------------

email = input("Enter your email address: ")

if " " in email:
    print("Invalid email: contains space")
elif email.count("@") != 1:
    print("Invalid email: missing '@' symbol.")
elif not (email.endswith(".com") or email.endswith(".edu") or email.endswith(".org")):
    print("Invalid email: domain must end with .com, .edu, or .org.")
else:
    at_index = email.find("@")
    username = email[:at_index]
    domain = email[at_index+1:]
    
    formatted_username = username.lower().replace("_", " ").replace(".", " ")
    
    print(f"Username: {formatted_username} | Domain: {domain}")