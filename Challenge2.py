# Write a Python program to check whether a given number is an Armstrong number or not.

def arm(num):
    total = 0
    str_num = str(num)
    power = len(str_num)
    for i in str_num:
        digit = int(i)**power
        total = total + digit
    return total

def arm_range(num1):
    total1 = 0
    str_num1 = str(num1)
    power1 = len(str_num1)
    total1 = sum(int(digit) ** power1 for digit in str_num1)
    return total1 == num1

# Main 1
n = int(input('enter the number :'))
if n == arm(n):
    print('number is armstrong')
else:
    print('number not armstrong')

# Main 2

lower = int(input("Enter start of range: "))
upper = int(input("Enter end of range: "))

print(f"Armstrong numbers between {lower} and {upper} are:")

for number in range(lower, upper + 1):
    if arm_range(number):
        print(number)
