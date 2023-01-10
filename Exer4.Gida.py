# A Python Program that will find the area of triangle
#this line of code below will store numbers from user input
firstSide = float(input('Enter first side: '))
secondSide = float(input('Enter second side: '))
thirdSide = float(input('Enter third side: '))
#this line of code below will calculate the semi-perimeter
answer = (firstSide + secondSide + thirdSide) / 2
#this line of code below will calculate the area
area = (answer *(answer -firstSide)*(answer -secondSide)*(answer -thirdSide)) ** 0.5 
print('The area of the triangle is %0.2f' %area)
print('Developed By: Crismark E. Gida \n \t\tBSIT IV')
