import heapq
from collections import * # deque
from functools import * # cmp_to_key

def cmp(a,b):
    if a>b:
        return -1
    else:
        return 1
  
arr=[5,3,1,3,7,12,41,9,51,8,1,9,12,41,13]

# arr.sort()
print("Origina; Arr ==> ",arr)
arr[0:5]=arr[0:5][::-1]  # reverse for i,j
print("Reverse of 0 to 5 ==> ",arr)

arr.sort(key=cmp_to_key(cmp))

print("Sorted Arr ==> ",arr)


# erase element from list

arr.pop(2) # second element will be removed
print("After pop ==> ",arr)
del arr[2] # fourth element will be removed
print("After del ==> ",arr)



dq=deque()

dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
dq.append(5)

print("Deque is: ",dq)
dq.pop() # pop from backside
dq.popleft() # pop from front side
print("Modified Deque is: ",dq)


pq=[]
heapq.heappush(pq,5)
heapq.heappush(pq,1)
heapq.heappush(pq,7)
heapq.heappush(pq,3)
heapq.heappush(pq,2)
heapq.heappush(pq,4)
heapq.heappush(pq,6)

print("Priority Queue is: ",pq)
heapq.heappop(pq)
heapq.heappop(pq)
print("Modified Priority Queue is: ",pq)


mp={1:"chuha",2:"billi",3:"kutta",4:"kutta-2",5:"kutta-3"}
print(mp[1])
mp[1]="Pidi chhua"
print(mp[1])

mp[10]=" Added element"

# get list of keys of dictionary
kk=list(mp.keys())
print("Keys are: ",kk)

# check  if any key is present in dictionary

def check_key(data,key):
    if key in data:
        return True
    return False

print(check_key(mp,1))
print(check_key(mp,16))


# Set in python  (Unordered Set)
s={1,2,3,4,5}
print("Set is: ",s)
s.add(6)
s.add(5)     # it will not add 5 as it is already present
s.remove(5)
print("Modified Set is: ",s)


print(check_key(s,91)) # falsee.






