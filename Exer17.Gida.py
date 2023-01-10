#A python program that will half pyramid using * 
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
print('Developed By: Crismark E. Gida \n \t\tBSIT IV')
