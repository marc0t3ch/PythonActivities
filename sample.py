#Get string from the User and lower all the characters
string = input("Enter a string: ").lower()


#Check if the string has enough character to compare
#Check if the first character and the last character are the same
if len(string) < 2:
  print("Not enough character to compare")
elif string[0] == string[-1]:
  print("Yes")
else:
  print("No")
