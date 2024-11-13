# Data Type or Object Type

# Number: 123, 3.14, 3+4j, 0b111, 0o777, 0x123,Decimal(10), Fraction(1,3)
# String: 'spam', "guido's", b'a\x01c', u'sp\xc4m'
# List: [1, [2, 'three'], 4.5], list(range(10))  (Array)
# Tuple: (1, 'spam', 4, 'U'), tuple('spam'), namedtuplen ()
# Dictioanry: {'food': 'spam', 'taste': 'yum'}, dict(hours=10) (key-value pairs)
# Set: set('abc'), {'a', 'b', 'c'} (unique items)
# File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')

# Boolean: True, False
# None: None
# Function,modules,classes (code objects)

# Advanced Types: Decorators, Generators,MetaProgramming, etc.

# Everything in Python is an object


# String

str="Hello World"
print(str)

# str[0]='A'  # Strings are immutable objects so we can't change the value of string it will give an error

# print(str[-1]) # (Negative indexing) It will give the last character of the string
# print(str[1:3]) # It will give the characters from index 1 to 2 
# print(str[1:]) # It will give the characters from index 1 to end


# print(dir(str)) # It will give the list of all the attributes and methods of the string object

# mylist=[1,2,3,4,5] # It is like an array in python
# print(mylist) # It will print the list

# mylist[0]=10 # We can change the value of list as it is mutable object
# print(mylist) # It will print the list

# print(mylist[1:3]) # It will give the elements from index 1 to 2
# print(mylist[1:]) # It will give the elements from index 1 to end


# myD ={1:'a',2:'b',3:'c'} # It is like a dictionary in pythons (key-value pairs)
# print(myD) # It will print the dictionary

# print(myD[1]) # It will give the value of key 1
# myD[1]='z' # We can change the value of key 1
# print(myD) # It will print the dictionary
# print(myD.keys()) # It will give the list of all the keys
# print(myD.values()) # It will give the list of all the values
# print(myD.items()) # It will give the list of all the key-value pairs
# myd["name"]="Ali" # We can add new key-value pair in the dictionary

# TIME COMPLEXITY -> O(1)


# myTuple=(1,2,3,4,5) # It is like a tuple in python
# print(myTuple[0])=10 # We can't change the value of tuple as it is immutable object

# len(myTuple) # It will give the length of tuple
# myTuple.count(1) # It will give the count of 1 in tuple


# tuple vs list
# tuple is immutable object
# list is mutable object
# tuple is faster than list
# list is slower than tuple
# list is used when we need to change the values of the elements


# mySet={1,2,3,4,5} # It is like a set in python
# print(mySet) # It will print the set
# mySet.add(6) # We can add new element in the set
# print(mySet) # It will print the set
# mySet.remove(6) # We can remove the element from the set
# print(mySet) # It will print the set
# unique elements in the set

# Time Complexity-> O(1)




