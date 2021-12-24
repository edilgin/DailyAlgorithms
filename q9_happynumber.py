"""
Q: Write an algorithm to determine if a number n is happy. A happy number is a number where when its digits are squared
and then summed repeatedly it equals 1. If it doesnt reach 1 then number is not happy.
"""

def checkHappy(number, count=1000):
    for i in range(count):
        number = sum([int(i)**2 for i in str(number)])
        if number == 1: return True
    return False

flag = checkHappy(100)
print(flag)
flag = checkHappy(19)
print(flag)
flag = checkHappy(2)
print(flag)