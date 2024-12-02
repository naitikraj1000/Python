# from functools import cmp_to_key
# from collections import *
# import heapq


# def cmp2(a,b):
#     if a>b:
#         return -1
#     else :
#         return 1

# def cmp(a,b):
#     if a[0] < b[0]:
#         return -1
#     elif a[0]>b[0]:
#         return 1
#     else:
#         if a[1] > b[1]:
#             return -1
#         elif a[1] < b[1]:
#             return 1
#         return 0
        
# def is_present_in_hash(hashmap,key):
#     if key in hashmap:
#         return True
#     return False
            
        
# data =[17,21,19,34,29,25,23,28,31,27,24,26,22,20,18]

# print("Data is: ",data)
# data.append(30) // push
# data.pop(index) // pop speicific index if not given last index will be popped
# print("Data is: ",data)


# data2=[ [2,1],[4,3],[2,3],[2,-2],[6,5],[8,7],[10,9],[12,11],[14,13],[16,15],[18,17],[20,19] ]
# len=len(data)

# print("Length of data is: ",len)

# data.sort(reverse=True)
# print("Sorted data is: ",data)

# data2.sort(key=cmp_to_key(cmp))
# print("Sorted data2 is: ",data2)




# hashmap={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}

# Unordered map in C++

# print("Hashmap is: ",hashmap) # print all the key value pairs
# print("Value of key 5 is: ",hashmap[5]) # print the value of key 5
# hashmap[11]="eleven" # add a new key value pair
# print("Hashmap is: ",hashmap)
# hashmap.pop(1) # remove the key value pair of key 1
# print("Hashmap is: ",hashmap)


# Ordered map in C++
# from sortedcontainers import SortedDict,SortedSet,SortedList  #(sortedList is Multiset in C++)
# print("shdb")

# ``for i in range(10,100,2):
#     print(i)``

# set1={1,2,3,4,5,6,7,8,9,10}

# print("Set is: ",set1)

# if 6 in set1:
#     print("6 is present in set")

# set2=SortedSet([10,81,12,33,21,45,67,89,23,34,56,78,90,11,22,33,44,55,66,77,88,99,100])

# print("Set2 is: ",set2)

# print("Back element is: ",set2[-1])

# print("First element is: ",set2[0])


# set3 = SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key=cmp_to_key(cmp2))


# print("Set3 is: ",set3)





# Priority Queue in Python


# min_heap=[]
# heapq.heappush(min_heap,10)
# heapq.heappush(min_heap,20)
# heapq.heappush(min_heap,15)
# heapq.heappush(min_heap,3)
# heapq.heappush(min_heap,2)
# heapq.heappush(min_heap,1)
# heapq.heappush(min_heap,7)
# heapq.heappush(min_heap,9)


# print("Min heap is: ",min_heap)


# print("Top element is: ",min_heap[0])
# heapq.heappop(min_heap)
# print("Min heap is: ",min_heap)
# print("Top element is: ",min_heap[0])




#pointers in python

# a=10
# b=10
# print("Address of a",id(a))
# print("Address of b",id(b))

# shallow and deep copy

# .copy() # shallow copy
# using slicing [:] # shallow copy

# Deep copy
# import copy
# copy.deepcopy( original_list )

# import copy
# ls=["HELLO", [11,12],1,12,2,13,3,14,4,15,5,16,6,17,7,18,8,19,9,20,10 ]
# temp_ls=ls.copy() # shallow copy
# temp2_ls=copy.deepcopy(ls) # deep copy
# print("Addr of Original Listt",id(ls)) 
# print("Addr of Shallow Copy List",id(temp_ls))
# print("Addr of Deep Copy List",id(temp2_ls))

# print("Addr of First Element of Original List",id(ls[0]))
# print("Addr of First Element of Shallow Copy List",id(temp_ls[0]))
# print("Addr of First Element of Deep Copy List",id(temp2_ls[0]))
    
 
# VVVI Concept    
# shallow copy and deep copy both changes the base address of the list but deep copy changes the address of the elements of the list which are mutable  



# class in Python 

# class student:
#     roll_no="2101CS40"
#     college="NIT Jalandhar"
#     def __init__(self,a):
#         print("Constructor called",self.roll_no)
    



# self is like this in c++


# a=student("test")
# print(a.roll_no)
# print(a.college)










queue=deque()
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

print("Deque is: ",queue)
queue.popleft()
print("Deque is: ",queue)




