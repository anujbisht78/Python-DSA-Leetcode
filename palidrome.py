# Palidrome Number

"""By reversing the digit and comparing with the number"""
# def palidrome(n):
#     temp=n
#     rev=0
#     while temp!=0:
#         digit=temp%10
#         rev=rev*10+digit
#         temp=temp//10
        
#     if rev==n:
#         print(n," is a Palidrome")
#     else:
#         print(n," is not a Palidrome")



"""Two pointer approach"""
def palidrome(n):
    i=0
    j=len(n)-1
    while i<j:
        if n[i]==n[j]:
            i+=1
            j-=1
        else:
            break
        
        return 1
    if 1:
        print("Its a palidrome")
    else:
        print("Its not a Palidrome")

n=int(input("Enter a number: "))
palidrome(n)