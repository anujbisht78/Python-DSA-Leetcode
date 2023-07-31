"""Prime Number"""

def isPrime(n):
    if n==1:
        return 0
    i=2
    while(i*i<=n):
        if n%i==0:
            return 0
        i+=1
        
    return 1

n=int(input("Enter a number:"))
if isPrime(n)==1:
    print(n,"is a Prime Number")
else:
    print("Not a Prime")
    