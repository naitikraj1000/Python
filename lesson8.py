from itertools import product

# lloops in Python

# ls=[1,2,3,4,5,6,7,8,9,10]

# for num in ls:
#     print(num)
    

# for i in range(1,10):
#     print(i)
    

# str="Hello World"
# rev_str=""
# for i in range(len(str)-1,0,-1):
#     rev_str+=str[i]
    # print(str[i])
    
    
    
# print(rev_str)
    
    
# while loop

# ans=1
# while (ans<=10):
#     print(ans)
#     ans+=1
    
 
# behind the scene of loop 
# iteration tool  (for,comprehension)
# (iterable Objects) --> (lists,file,strings,etc)
# __next__

f=open("test.txt")
for line in f:
    print(line)
    
    print( f is iter(f))  // True
    
    # f is itself iterable object


myList=[1,2,3,4,5,16,7,8,9,10]
myiter=iter(myList)
print(myiter.__next__(),myiter)
print(myiter.__next__(),myiter)
print(myiter.__next__(),myiter)
print(myiter.__next__(),myiter)
print(myiter.__next__(),myiter)
print(myiter.__next__(),myiter)

print("Adress of Base List",hex(id(myList)))
print((myiter is myList)) ## False

# myList is not iterable object but myIter is iterable object

# Adress of myIter is samae but the value is changing 