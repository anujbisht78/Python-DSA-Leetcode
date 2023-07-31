"""
Trailing Zeros in factorial means counting the zeros in the result
"""
def trailzero(n):
    i=1
    fact=1
    while i<=n:
        fact=fact*i
        i+=1
        

    count=0
    while (fact%10==0):
        count+=1
        fact=fact//10
    
    return count
    
    

n=int(input("Enter a Number: "))
print("No of Zeros are: ",trailzero(n))
    
