# A python program that will find the largest number among the three input numbers
firstNum = float(input("Enter first number: "))
secondNum = float(input("Enter second number: "))
thirdNum = float(input("Enter third number: "))
if (firstNum >= secondNum) and (firstNum >= thirdNum):
   largestNum = firstNum
elif (secondNum >= firstNum) and (secondNum >= thirdNum):
   largestNum = secondNum
else:
   largestNum = thirdNum
print("The largest number is", largestNum)
print('Developed By: Crismark E. Gida \n \t\tBSIT IV')
