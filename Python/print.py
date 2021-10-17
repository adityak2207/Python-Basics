#Check if a number is prime or not

n = int(input("Enter a number : "))
if(n==1):
    print(n,"is not a prime number")
i=2
is_prime = 1
while(i!=n):
    if(n%i == 0):
        is_prime = -1
        break
    i=i+1
    
if(is_prime == 1):   
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")