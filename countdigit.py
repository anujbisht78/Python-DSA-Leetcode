# Count Digit
"""Given a number N. Count the number of digits in N which evenly divides N.

Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided."""

def evenlyDivides(N):
    n=str(N)
    count=0
    for i in n:
        if int(i)==0:
            continue
            
        elif N%int(i)==0:
            count+=1
            
    return count
    
N=int(input("Enter the Number: "))
print("Number of Digit are",evenlyDivides(N))

    