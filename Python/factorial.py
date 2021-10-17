#Write a program to print the factorial of a given number

def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

n = int(input("Enter a given number : "))
print("The factorial of",n,"is",fact(n))
