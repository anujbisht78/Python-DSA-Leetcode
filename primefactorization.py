"""Prime Number"""

def isprime(x):
    if x==0:
        return 0
    i=2
    while (i*i<=x):
        if x%i==0:
            return 0
        i+=1
    return 1
    
def prime(n):
    for i in range(2,n):
        if isprime(i):
            x=i
            while n%x==0:
                print(i,end=" ")
                x=x*i
                # x=i+1
                
            

n=int(input("Enter the Number:"))
print(prime(n))