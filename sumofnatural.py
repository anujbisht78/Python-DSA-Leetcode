#sum of n natural Numbers

# def sum(num):
#     return (num*(num+1))/2

def sumofn(num):
    sum=0
    i=1
    while i<=num:
        sum=sum+i
        i=i+1
          
    return sum

num=int(input("Enter the Number: "))
print("Sum is:",sumofn(num))
