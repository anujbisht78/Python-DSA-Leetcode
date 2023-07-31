# Reversing a Number

def reverse(n):
    rev=0
    temp=n
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
        
    return rev

n=int(input("Enter a Number: "))
print("Reverse is",reverse(n))
