"""Least Common multiple"""

A=int(input("Enter the value of a:"))
B=int(input("Enter the value of b:"))

rem=1
dividend=max(A,B)
divisor=min(A,B)
while rem!=0:
    rem=dividend%divisor
    if rem!=0:
        dividend=divisor
        divisor=rem
lcm=(A*B)/divisor   
       
        
print("GCD is",lcm)