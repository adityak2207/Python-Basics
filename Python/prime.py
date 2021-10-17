#Check if a number is prime or not 
                                    # ~"KrevoL"

n=int(input("Enter a number : "))
i=2
is_prime = 1

while(i!=n):
    if(n%i==0):
        is_prime = -1
        break
    i=i+1
    
if(is_prime > 0):
    print(n,"is prime")
else:
    print(n,"is not prime")