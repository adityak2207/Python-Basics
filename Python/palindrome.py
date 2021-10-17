#Write a program to check whether the given string is a palindrome or not

def isPalindrome(str):
    j = len(str)
    for i in range (0,len(str)):
        if(str[i] == str[j-1]):
            flag = True
            j = j-1
        else:
            flag = False
            break
    return flag
        

str = input("Enter a string : ")
res = isPalindrome(str)

if res:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")