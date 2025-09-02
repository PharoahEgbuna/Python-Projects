#This code takes two user inputs and checks if they are anagrams

string1 = list(input("Enter first string: ").lower().replace(" ", ""))
string2 = list(input("Enter second string: ").lower().replace(" ", ""))


for char in string1:
    if char in string2:
        string2.remove(char)
        is_anagram = "Anagrams"
    else:
        is_anagram = "Not anagrams"
        break 
    
print(is_anagram)