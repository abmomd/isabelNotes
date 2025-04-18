# What is a string ? --> Word or a sentence.
# What is an integer ? --> Number

x = "Hello"
print(x)
print("I am Aryavansh.")

para = '''I am Aryavansh.
I live in Delhi. 
I like Maths. '''

print(para)

name = "Aryansh"
# Index of string always starts with 0.

print("First Character of String name is: " + name[0])
print("Fifth Character of String name is: " + name[4])

#Finding the length of the string.

print("The length of the string is: " + str(len(x)))

sentence = "I am Aryavansh. I live in Delhi. I like Maths"

#Checks something specific is present in the entire string.
print("Mumbai" in sentence)

if "Delhi" in sentence:
    print("Yes, Delhi is present in the sentence")

#Checks something specific is not present in the entire string.
print("Mumbai" not in sentence)

# Slicing of Strings.

a = "Hello, World!"
#    01234567891011
print(a[7:12])
#What index to print "ello," ?
print(a[1:6])
#this prints (6-1) = 5 letters starting from index 1.

b= "Torchbearer Academy!"
#print "bearer"
print(b[5:11])

# I want everything after the letter b --> bearer Academy
print(b[5:])

# print only Torch
print(b[:5])

#Modification of Strings

a = "hello, india!"
print(a.upper())
b = "HELLO WORLD!"
print(b.lower())
c= "         How are you feeling today      "
print(c)
#Remove the whitespaces from the front and end
print(c.strip())

d = "How are you ?"
# replace a letter 'H' to 'W' in the string
print(d.replace("H", "W"))

colours ="Red;Blue;Green;Yellow;Purple;White;Black"
print(colours.split(";"))






