# Number in Python
import math
import random

x=10
y=12.5
z=18

print(x==y) # It will give False    (It will compare the values of x and y)
print(x is y) # It will give False  (It will compare the address of x and y)
print(x!=y) # It will give True    (It will compare the values of x and y)

print((x<y<z)) # It will give True  (It will compare the values of x,y and z)
# (x<y and y<z) is same as (x<y<z)


var1=10.23
print(math.floor(var1)) # It will give 10 (It will give the floor value of the number)
print(math.trunc(var1)) # It will give 10 (It will give the trunc value of the number)


 # other base in Numner
print(0b1010) # It will give 10 (It will give the value of binary number)
print(0o12) # It will give 10 (It will give the value of octal number)
print(0x0A) # It will give 10 (It will give the value of hexadecimal number)

oct(10) # It will give the octal value of the number
hex(10) # It will give the hexadecimal value of the number
bin(10) # It will give the binary value of the number


int("1010",2) # It will give 10 (It will give the decimal value of the binary number)
int("0b1010",2) # It will give 10 (It will give the decimal value of the binary number)
int("12",8) # It will give 10 (It will give the decimal value of the octal number)

print(random.random()) # It will give the random number between 0 and 1

random.randint(1,10) # It will give the random number between 1 and 10

l1=['lemmon','apple','banana','orange'] # It is a list
print(random.choice(l1)) # It will give the random element from the list

# 0.1+0.1+0.1 - 0.3
# 5.551115123125783e-17
# why it is not equal to 0
# because of the floating point arithmetic in python
# floating point arithmetic is not exact
# it is not a bug in python
# it is a limitation of the floating point arithmetic
# it is a limitation of the hardware
# it is a limitation of the computer



