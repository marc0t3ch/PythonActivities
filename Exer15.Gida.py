# A python program that will count the number of each vowels in a string
# string of vowels
vowels = 'aeiou'
ip_str = input("Enter a string: ")
# make it suitable for caseless comparisons
ip_str = ip_str.casefold()
# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)
# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1
print(count)
print('Developed By: Crismark E. Gida \n \t\tBSIT IV')
