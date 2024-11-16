# def square(n):
#     return n*n


# squared = square(int(input("Enter a number: ")))
# print(squared)



# def sum_all(*args):
#     print(type(args))
#     return sum(args)
    
    
# print(sum_all(1,2,3,4,5,6,7,8,9,10)) 




def fact(n):
    if n==0:
        return 1
    else :
        return n*fact(n-1)
    
    
print(fact(int(input()))) # 120    