### **Everything in Python is an Object**
# 1. **All entities** (numbers, strings, lists, functions, classes, modules, etc.) are **instances of classes** and derive from the base class `object`.
# 2. **Primitive types** like `int`, `float`, `str`, `bool`, etc., are objects.
# 3. **Functions and classes** are also objects, allowing them to be passed as arguments, assigned to variables, and returned from other functions.
# 4. Python is a **fully object-oriented language**, enabling dynamic behavior and flexibility.
# 5. This unified object model makes Python powerful and consistent in handling all data types.

x = 42
print(f"Address of x: {hex(id(x))}")

x=482
print(f"Address of x: {hex(id(x))}")  # The address of x has changed


            # |
            # |
            # |  [42]  <---- x ( It deletes the memory of 42 and creates a new memory for 482)
            # |
            # |
            # |   [482]  <---- x
            # |
            # |

# the address of x has changed becuase of the working of the garbage collector in python
# the garbage collector is responsible for managing the memory in python
# the garbage collector is responsible for deleting the memory that is no longer needed
# every thing in python is an object and every object has an address in memory
# x just point to the address of the object in memory
# There is concept of Mutable and Immutable objects in python
# X is int which is immutable object(immutable objects are those objects whose value can not be changed)
# that's why when we change the value of x the address of x also changes (becuase we can't change the value at the same address as it is immutable object)


 # 1. **Mutable objects** can be changed after creation, while **immutable objects** cannot.
#   Mutable Objects: list, dict, set, byte array
#   Immutable Objects: int, float, complex, string, tuple, frozen set [note: immutable version of set], bytes




