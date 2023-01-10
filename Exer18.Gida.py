#A python program that will half pyramid using numbers 
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")
print('Developed By: Crismark E. Gida \n \t\tBSIT IV')
