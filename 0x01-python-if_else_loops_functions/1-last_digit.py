#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
answer = number % 10

if number < 0:
    answer = ((-number % 10) * (-1))

if answer > 5:
    print(f"Last digit of {number} is {answer} and is greater than 5")
elif answer == 0:
    print(f"Last digit of {number} is {answer} and is 0")
elif (answer < 6) and (answer != 0):
    print(f"Last digit of {number} is {answer} and is less than 6 and not 0")
