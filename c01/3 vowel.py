word =str(input("Enter the word :"))
print("The original string is : "+word)
print("The vowel are : ",end="")
for i in word:
   if i in 'aeiouAEIOU':
      print([i],end=" ")

