# singe_quote = 'Hello' #(first character)
# double_quote = "World" #(first character)
# triple_single_quote = """This is a multi-line"""

# test = "Python Programming" 

# print(test[0])  # first character
# print(test[-1]) # last character
# print(test[0:6]) # first 6 characters"
# print(test[:6])  # from 7th character to end
# print(test[7:])  # from 7th character to end

# name = " alice "

# print(len(name))  # length of the string
# print(name.strip())  # remove leading and trailing whitespace
# print(name.upper())  # convert to lowercase
# print(name.lower())  # convert to uppercase
# print(name.title())  # convert to title case
# print(name.replace("alice", "Bob"))

# name = "Syamil"
# age = 30

# message_1 = f"My name is {name} and I am {age} years old."
# message_2 = "My name is {} and I am {} years old.".format(name, age)   
# message_3 = "My name is %s and I am %d years old." % (name, age)

# print(message_1)
# print(message_2)
# print(message_3)

# Build a simple text analyzer that can count the number of characters, words, and lines in a given text.
text = """Python is a powerful programming language.It's easy to learn and versatile!
Your can use it for web development, data science, and automation. The syntax is clean and readable.
This make Python perfect for beginners and expertalike alike."""

char_count = len(text)
char_count_no_spaces = len(text.replace(' ', ''))
word_count = len(text.split())
sentence_count = text.count('.') + text.count('!') + text.count('?')

print(f"Character count (including spaces): {char_count}")
print(f"Character count (excluding spaces): {char_count_no_spaces}")   
print(f"Word count: {word_count}")
print(f"Sentence count: {sentence_count}")

