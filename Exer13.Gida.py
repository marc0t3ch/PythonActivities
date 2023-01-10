# A python program that will display the Fibonacci sequence
def recursiveFibonacci(num):
   if num <= 1:
       return num
   else:
       return(recursiveFibonacci(num-1) + recursiveFibonacci(num-2))
nterms = 10
# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recursiveFibonacci(i))
print('Developed By: Crismark E. Gida \n \t\tBSIT IV')
