# practice function

# find anagram using function

def anagram(name1,name2):
   if sorted(name1) == sorted(name2):
        print("anagram !!")
   else:
        print("not anagram ..")
word1 = str(input("Enter a name1 : "))
word2 = str(input(("Enter a name2 : ")))
anagram (name1 = word1,name2 = word2)  # called tha function

# find palindrome or not

def palindrome(word):
    if word == word[::-1]:
        print("palinrome !!")
    else:
        print("not palindrome ..")
name = str(input("Enter a name :"))
palindrome(word = name) # called tha function