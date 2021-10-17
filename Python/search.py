#Write a program to search a number in a given set of numbers

number_list = input("Enter n numbers : ")

number_list = number_list.split()

for i in range(0,len(number_list)):
    number_list[i] = int(number_list[i])

key = int(input("Enter the value to be searched in the list : "))

try:
    print("The value",key,"was found in postion",number_list.index(key) + 1)
except:
    print("The element was not found")
