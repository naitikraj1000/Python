# list is array (mutable)
# tuple is same as list (immutable)
# dictionary is like map (mutable)

# conditional statements

age=int(input("Enter your age: "))
print("Your age is: ",age)

if(age<13):
    print("You are a child")
elif (age<20):
    print("You are a teenager")
elif age<60:
    print("You are an adult")
else:
    print("You are a senior citizen")

cnt=">18" if age>=18 else "<18"

    

