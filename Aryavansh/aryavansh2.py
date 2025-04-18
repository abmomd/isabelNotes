#String Concatenation --> Combining two or more strings using + operator
a  = "Hello"
b = "World!"
c = "India!"
d = "Aryavansh"
print(a+" "+b+" "+d)

#Format Strings
# {} --> Called as Placeholders

age = 15
txt = f"My name is Mike, I am {age}" 
txt2 = "My name is Mike, I am " + str(age)

print(txt)

price = 47
txt = f"The price is {price} dollars."
print(txt)

price =57
txt = f"The price is {price:.3f} dollars."
print(txt)

# Apple costs 120 Rs a kilo. And I want to buy 4kgs.

totalPrice = f"The total cost will be {120*4} rupees."
print(totalPrice)

#Escape Characters
# I want to print double quotes in the printing statement.

txt = "We are the so-called \"Vikings\" from the North."
print(txt)

#Insert a backslash --> \
txt = "This should insert \ (backslash)"
print(txt)

#Printing a new line
txt="Hello\nWorld!"
print(txt)

#String Methods --> Useful Functions

sentence = "this is a sentence."
print(sentence.capitalize())
#capitalize() --> Makes the first letter capital

sentence = "THIS IS A SENTENCE."
print(sentence.casefold())
#casefold() --> Converts the string to lowercase.

sentence ="This is a python programming class"
print(sentence.endswith("class"))
#endswith() --> Return True False if the last part matches the condition.

print(sentence.find("is"))
#find() --> Gives the first index of the string you want to find.

sentence = "This includescharactersabcandnumbers123"
print(sentence.isalnum())
#isalnum() --> Checks if the string is ONLY alphanumeric or not.

sentence = "alphabets"
print(sentence.isalpha())
#isalpha() --> Check if the string contains ONLY alphabets.

sentence="3215649864"
print(sentence.isdigit())
#isdigit() --> Check if the string contains ONLY digits.

# Write a program to check if a number is even or not.
# / -->Division
# % --> Remainder

num = 57

#method 1 using Remainder
rem = num%2
if rem == 0:
    print("It's an Even Number.")
else:
    print("It's an odd number.")

#Write a program to find the last digit of a number.
#Example num = 7236549 --> Last digit = 9
#Example num = 236492 --> Last digit = 2

num = 4578546
lastDigit = num%10

print(lastDigit)
