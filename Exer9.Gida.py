# A python program that will find the L.C.M. of two input number
# This function computes GCD 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1= float(input("Enter First Number: "))
num2 =  float(input("Enter Second Number: "))
print("The L.C.M. is", compute_lcm(num1, num2))
print('Developed By: Crismark E. Gida \n \t\tBSIT IV')
