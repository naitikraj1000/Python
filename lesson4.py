# Internal working of python | Copy, reference counts, slice

var1=10000
var2=10000

print(f"Address of var1: {hex(id(var1))}")
print(f"Address of var2: {hex(id(var2))}")
print(var1 is var2)

# The address of var1 and var2 is same because of the concept of reference counting in python
# It optimizes the memory by pointing the same address to the same value

# ref_count (reference count) is the number of references to the object in memory

# In Python data type is not explicitly defined for the variables
# It automatically assigns the data type to the value of the variable in memory


# (Garbage collector) is responsible for managing the memory in python
# It deletes the memory that is no longer needed
# It deletes the memory of the objects that have reference count 0
# It deletes the memory of the objects that are no longer needed
# It gives Number anf String a special treatment in python, It doesn't clear the memory of Number and String objects immediately

var3=10
print(f"Address of var3: {hex(id(var3))}")
var3=var3+20
print(f"Address of var3: {hex(id(var3))}")

# The address of var3 has changed because the value of var3 has changed


# Memory in Mutable Objects
# It will create a new memory for the new value of the object
# but if u give the same reference to the new object it will point to the same address of the old object

mylist1=[1,2,3,4,5]
# mylist2=[1,2,3,4,5] # It will create a new memory for mylist2
mylist2=mylist1 # Shallow copy (It will point to the same address of mylist1)
mylist2[0]=191 # It will change the value of mylist1 also in memory
mylist1.append(6) # It will change the value of mylist2 also in memory

print(f"Address of mylist1: {hex(id(mylist1))}",mylist1)

print(f"Address of mylist2: {hex(id(mylist2))}",mylist2)

# address value of mylist1 and mylist2 is same or (mylist1 and mylist2) are pointing to the same address


mylist3=[1,2,3,4,5]
mylist4=mylist3 # it will point to the same address of mylist3

mylist4=[182,2,3,4,5] # It will create a new memory for mylist4
# even u give mylist4=[1,2,3,4,5] it will create a new memory for mylist4 as it is mutable object
print(f"Address of mylist3: {hex(id(mylist3))}",mylist3)
print(f"Address of mylist4: {hex(id(mylist4))}",mylist4)

# address value of mylist3 and mylist4 is different or (mylist3 and mylist4) are pointing to the different address


# in SLICE it will create a new memory for the new object
mylist5=[1,2,3,4,5]
mylist6=mylist5[:] # It will create a new memory for mylist6
mylist6[0]=191 # It will not change the value of mylist5
print(f"Address of mylist5: {hex(id(mylist5))}",mylist5)
print(f"Address of mylist6: {hex(id(mylist6))}",mylist6)


# x="Hello"
# y=x
# y="World"
# print(f"Address of x: {hex(id(x))}",x)
# print(f"Address of y: {hex(id(y))}",y)

# as string is immutable object so it will create a new memory for the new object



# In short 
# Immutable object can't change their values so if the value repeat it will point to the same address in the case of mutable object 
# But Not always in case of immutable object if number are large it will create a new memory for the new object
# When values are the same, they often point to the same memory address (but this is an optimization, not a guarantee)

# for Mutable object it will create a new memory for the new object as the value can be changed in the same memory





t1=[1,2,3,4,5]
t2=t1[:]

print(f"Address of t1: {hex(id(t1))}",t1)
print(f"Address of t2: {hex(id(t2))}",t2)


print( t1[0] is t2[0]) # It will give True as the value of t1 and t2 is same so it will point to the same address
print( id(t1[0]))
print( id(t2[0]))



# def add_two_to_list(my_list=[]):
    
#     my_list.append(2)
#     return my_list
# first = add_two_to_list()
# print(first)
# second = add_two_to_list()
# print(second)


# Note if we pass default parameter it will point to the same address of the default parameter and used the same memory so it will change the value of the default parameter


