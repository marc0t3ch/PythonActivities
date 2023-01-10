# A python program that will sort the words alphabetically in a form of string provided by the user

# To take input from the user
myStr = input("Enter a string: ")
#breakdown the string into a list of words
words = [word.lower() for word in myStr.split()]
# sort the list
words.sort()
# display the sorted words
print("The sorted words are:")
for word in words:
   print(word)
print('Developed By: Crismark E. Gida \n \t\tBSIT IV')
