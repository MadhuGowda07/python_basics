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


#Fibonacci Sequence
n_terms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if n_terms <= 0:
    print("Please enter a positive integer")
elif n_terms == 1:
    print("Fibonacci sequence up to", n_terms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1                                  
#output
'''
How many terms? 4
Fibonacci sequence:
0
1
1
2
'''


#Prime Number
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
#output
'''
Enter a number: 5
5 is a prime number
'''


#Palindrome
string = input("Enter a string: ")

# Check if string is equal to its reverse
if string == string[::-1]:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
#output
'''
Enter a string: 121 
121 is a palindrome
'''

#Number Guessing Game
import random

number_to_guess = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")
        break
#output
'''
Guess the number between 1 and 100!
Enter your guess: 50
Too low!
Enter your guess: 70
Too low!
Enter your guess: 85
Too low!
Enter your guess: 92
Too low!
Enter your guess: 97
Too high!
Enter your guess: 94
Too high!
Enter your guess: 93
Congratulations! You've guessed the correct number in 7 attempts.
'''

#spy number
def is_spy_number(num):
    num_str = str(num)
    digit_sum = 0
    digit_product = 1
    for digit in num_str:
        digit_int = int(digit)
        digit_sum += digit_int
        digit_product *= digit_int
    return digit_sum == digit_product
number = int(input("Enter a number: "))
if is_spy_number(number):
    print(f"{number} is a spy number.")
else:
    print(f"{number} is not a spy number.")

#output
'''
Enter a number: 34
34 is not a spy number
'''


# A simple Python function
def fun():
    print("Welcome to GFG")
fun()            #Welcome to GFG


#
