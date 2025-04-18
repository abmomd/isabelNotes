
# list = [5,2,7,2,4,1,32,52,43,67]
# list.sort( reverse=True)
# print(list)

list1 = ["Tokyo", "Delhi", "MUMBAI", "LONDON", "Paris", "Moscow", "Berlin", "Madrid","Los Angeles", "Las Vegas" ]
list1.sort(reverse = True)
print(list1)

list2 = ["India", "Japan", "China", "USA", "Russia", "Germany", "France"]

country = list2[4:]
country = list2.copy()

print(country)

city = list1.copy()

newJoinedList = city + country
print(newJoinedList)

list1 = [5,4,2,4,2,4,3,2,3,4,5,2,3,4]
list2 = ["a" , "b", "c"]

for x in list2:
    list1.append(x)

print(list1)

list2.extend(list1)
print(list2)

list2.clear()
print(list2)

print(list1.count(2))
list1.reverse()
print(list1)


# TUPLE --> Which can not be changed/ IMMUTABLE LIST.

thistuple = ("apple", "banana", "cherry","orange")



# thistuple[1] = "blackcurrant" # This will give an error because tuple is immutable.

print(thistuple[: 2])
print(thistuple[2])
print(len(thistuple))

tuple1 = ("apple",)
print(type(tuple1))

# NOT A TUPLE
tuple2 = ("apple")
print(type(tuple2))


# Workaround to change tuple values

x = ("apple", "banana", "cherry")
y = list(x) 
print(type(y))
print(y)
y[1] = "kiwi"
print(y)
x = tuple(y)
print(type(x))
print(x)

#Workaround to add tuple values
x = ("apple", "banana", "cherry")
y = list(x) 
print(type(y))
print(y)
y.append("kiwi")
print(y)
x = tuple(y)
print(type(x))
print(x)

# Add Tuple to Tuple
z = ("orange",)

x += z
print(x)

#Workaround to remove tuple values
x = ("apple", "banana", "cherry")
y = list(x) 
print(type(y))
print(y)
y.remove("banana")
print(y)
x = tuple(y)
print(type(x))
print(x)

del x
# print(x)

#Unpacking Tuples

cities = ("Paris","Delhi","Mumbai")

(city1,city2,city3) = cities

print(city1)
print(city2)
print(city3)


#Unpacking Tuples

cities = ("Paris","Delhi","Mumbai")

(city1,city2,*city3) = cities

print(city1)
print(city2)
print(city3)
print(type(city3))

countries = ("India","Japan","China","USA","Russia","Germany","France")
(first,second, *middle, last) = countries
print(first)
print(second)
print(middle)
print(last)


# Loops in Tuples

# for x in countries:
#     print(x)

# for i in range(len(countries)):
#     print(countries[i])

i = 0

while i < len(countries):
    print(countries[i])
    i += 1

joinedTuple = countries + cities
print(joinedTuple)

multiple2 = cities * 2
print(multiple2)

print(multiple2.count("Delhi"))

# SETS --> Unordered collection of unique elements.
# No duplicates allowed.

thisset ={"guitar" ,"drums", "piano", True , 1 ,2, False , 0 , 0}
print(thisset)
print(type(thisset))
print(len(thisset))

newSet = set(("apple", "banana", "cherry"))
print(newSet)

# Set can be accessed only using the For loop.

for x in thisset:
    print(x)
print("apple" in thisset)
print("banana" not in thisset)
print("guitar" in thisset)

print(newSet)

newSet.add("orange")
print(newSet)

# Add one set to another using the update() method.

thisset.update(newSet)
print(thisset)

thisset.update({"violin","flute","kiwi"})
print(thisset)

thisset.remove("guitar")
thisset.remove("drums")
thisset.remove("piano")
thisset.discard("guitar")
print(thisset)

x = thisset.pop()
print(x)
print(thisset)

thisset.clear()
print(thisset)

del thisset

set1= {1,2,3,4,5}
set2= {4,5,6,7,8}
newset1 = {2,1,2,43,6,8,9,4,3,3,2}
set3 = set1.union(set2,newset1)
print(set3)

# Using | symbol
set4 = set1 | set2 | newset1
print(set4)

set5  = set1.intersection(set2)
print(set5)

set6 = set1 & set2
print(set6)

