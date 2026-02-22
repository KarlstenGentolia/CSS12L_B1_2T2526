# Dela Rosa_Danielle Charisse_MP4

# Word Pyramid

# Ask for a word and an integer N. Print the word in a growing pyramid pattern up to N times.
# Skills: String multiplication (*), input conversion, loops

# word = Water

word = input("Enter a word: ").strip()
n = int(input("Enter a number: "))

# Generate pyramid
print("\nOutput:")
for i in range(1, n + 1):
    print(word * i)
    