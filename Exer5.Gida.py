# A python program that will solve the quadratic equation ax**2 + bx + c = 0
# import complex math module
import cmath
firstNum = float(input('Enter the First Number: '))
secondNum = float(input('Enter the Second Number: '))
thirdNum = float(input('Enter the Third Number: '))
# This line of code below will calculate the discriminant
answer = (secondNum**2) - (4*firstNum*thirdNum)
# This line of code below will find two solutions
sol1 = (-secondNum-cmath.sqrt(answer))/(2*firstNum)
sol2 = (-secondNum+cmath.sqrt(answer))/(2*firstNum)
print('The solution are {0} and {1}'.format(sol1,sol2))
print('Developed By: Crismark E. Gida \n \t\tBSIT IV')
