#area_of_circle
import math
def area(radius):
    if x<0:
        return 0
    else:
        Area=math.pi*x*x
        return Area
radius=7
result=area(radius)
print(result)        #314.1592653589793


#Sum of Two Numbers
num1 = 2
num2 = 3
sum = num1 + num2
print(sum)      #5

#Even or Odd
num = 7
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")    #7 id Odd

#Largest Number
num1 = 1
num2 = 2
num3 = 3
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print(largest)      #3


#Factorial
num = 4
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")        #The factorial of 4 is 24


#Sum of Digits of a Number
num = 123
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10
print("The sum of the digits is:", sum_of_digits)      #6

