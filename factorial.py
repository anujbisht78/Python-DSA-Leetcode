# Factorial Number

"""Recursive approach"""
# def fact(n):
#     if n==0:
#         return 1
#     return n*(fact(n-1))

def fact(n):
    i=1
    prod=1
    while i<=n:
        if n==0:
            return 1
        else:
            prod=prod*i
            i+=1 
    
    return prod

n=int(input("Enter a Number: "))
print("factorial is",fact(n))
