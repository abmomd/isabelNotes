#range(5) --> [0, 1, 2, 3, 4]
#range(8)--> [0, 1, 2, 3, 4, 5, 6, 7]
#range(2, 10) --> [2, 3, 4, 5, 6, 7, 8, 9]

# Write a statement 15 times.
#LOOPS
# For a particular amout of time, we want to execute same statement everytime.

# For loop and a while loop.
# For loop --> Used when we know how many times we want to execute the loop.
# WHile loop -->  Used when we don't know how many times we want to execute the loop.

num = 3479024
n = 7

# num%10 --> This will give me the last digit.
# num//10 --> 347902
# keep on repeating this process until num becomes 0.
# Can not use for loop --> Because we do not know number of digits.

# Print all the digits of the number.

for i in range(n):
    rem = num%10
    print(rem) 
    num = num//10
    print(num)

# while num > 0:

#     rem = num%10
#     print(rem) 
#     num = num//10
#     print(num)

list = ["Tokyo", "Delhi", "Mumbai", "London"]

# i is an index variable.
for i in range(len(list)):
    print(list[i])
    # print(i)

# x is the element variable.
for x in list:
    print(x)

ind = 0
while ind < len(list):
    print(list[ind])
    ind += 1


#List Comprehension
# When you want to create a new list based on an existing list.

list = ["Tokyo", "Delhi", "MUMBAI", "LONDON", "Paris", "Moscow", "Berlin", "Madrid","Los Angeles", "Las Vegas" ]

newList =[] # All Cities which will have letter "M"

for city in list:
    if "M" in city:
        newList.append(city)

print(newList)

newList1 =[city for city in list if "L" in city]
print(newList1)

newList2 =[city for city in list if len(city) >= 6]
print(newList2)


newList3 = [city  for city in list if len(city) >= 6 and  city == city.upper()]
#           
print(newList3)

# if condition is true, then it will simply insert the city into the list.
# if condition is flase, then it will insert "Not Upper Case" into the list.

# if (city == city.upper()):
# "Mumbai" == "MUMBAI" ==> False
# "DELHi" == "DELHI" ==> True

