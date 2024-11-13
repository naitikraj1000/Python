# String in Python
str="0123456789"
print(str[0]) # It will give the character at index 0

# print(str[0:5]) # It will give the characters from index 0 to 4

# print(str[0:5:2]) # It will give the characters from index 0 to 4 with step 2

# str.replace("0","A") # It will replace the 0 with A in the string

# upper() method is used to convert the string into upper case
# lower() method is used to convert the string into lower case
# title() method is used to convert the string into title case

# print(str.upper()) # It will convert the string into upper case


chai = "Lemon, Ginger, Honey, Water"
# convert the string into list
# split() method is used to convert the string into list
# split() method takes two arguments
# 1. separator
# 2. maxsplit

print(chai.split(", ")) # It will convert the string into list

#find() method is used to find the index of the substring in the string
#find() method takes two arguments
#1. substring
#2. start index
print(chai.find("Ginger")) # It will give the index of Ginger in the string

#Length of the string
# print(len(chai)) # It will give the length of the string
