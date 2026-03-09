""" 
1) Sum of numbers from 1 to n
3) Reverse a number
4) Reverse a string
12) Generate multiplication table of a number
15) Remove spaces from a string
16) Replace vowels with *
"""

# 1)
'''n = int(input("Enter the value for n: "))
sum = n * (n+1)//2
print(f"The sum of all numbers from 1 to {n} is {sum}")'''

# 3)
'''n = int(input("Enter a number: "))
rev = 0
while n>0:
    digit = n%10
    rev = rev*10+digit
    n = n//10

print("The reversed number is: ", rev)'''

# 4)
'''
s = input("Enter a string of your choice: ")
print("Reversed string: ", s[::-1])'''

# 12)
'''
n = int(input("Enter the number: "))
print(f"The multiplication table of number {n} is:")
for i in range(1,10):
    tab = i*n
    print(tab)'''

# 15)
'''
s = input("Enter a string with spaces: ")
spaceless = s.replace(" ","")
print("The string without spcaes is: ", spaceless)'''

# 16)
'''
s = input("Enter any string: ")
output = ""
for ch in s:
    if ch in "aeiouAEIOU":
        output += "*"
    else:
        output += ch

print("The string after replacing the vowels with *: ", output)'''