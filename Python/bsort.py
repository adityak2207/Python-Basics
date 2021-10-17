#Write a program to sort n numbers

number_list = input("Enter n elements : ")
number_list = number_list.split()

for i in range (0, len(number_list)):
    number_list[i] = int(number_list[i])

number_list.sort()

for i in range(0, len(number_list)):
    print(number_list[i], end=" ")