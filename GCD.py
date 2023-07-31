"""Greates Commom Divisor"""

A=int(input("Enter the value of a:"))
B=int(input("Enter the value of b:"))

# mx=max(a,b)
# i=1
# ans=0
# while i<=mx:
#     if a%i==0 and b%i==0:
#         ans=i
#         i+=1
#     else:
#         i+=1

"""Euclidean Algo"""
rem=1
dividend=max(A,B)
divisor=min(A,B)
while rem!=0:
    rem=dividend%divisor
    if rem!=0:
        dividend=divisor
        divisor=rem
    
       
        
print("GCD is",divisor)
        




