#Write a program to concatenate two words, find the length of a word and to search the element
#in a sentence and also compare words

word1 = input("Enter the first word : ")
word2 = input("Enter the second word : ")

word3 = word1 + word2
print(word1,"+",word2,"=",word3)

print("The length of", word3, "=", len(word3))

sub_word = input("Enter the substring to be searched in "+ word3 + ": ")

if sub_word in word3:
    print(sub_word, "found in", word3)
else:
    print(sub_word, "not found in", word3)

word1,word2 = input("\nEnter two words to compare : ").split()

if(word1 == word2):
    print("The words are the same")
else:
    print("The words are different")