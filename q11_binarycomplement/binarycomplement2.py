"""
Q: Given a number find its binary complement
A: Algorithm is slightly complex so let me break it down:
    I want to find complement by using binary shift right operations.
    1- We will have a count variable to see at which digit we are working on. This count is important because if we
    dont know which digit we are at, then we wont be able to find the right value.
    2- Comp variable will be initialized to 0. This is the variable that holds complements value and it will be
    increased as we look at individual digits of the original number.
    3- We will define a loop and inside do the following:
        A) num & 1 returns the last digit of the num. If it is one we skip. If it is zero we do the following: Find
        the value that should be added by doing 2**count. 2**count returns the value of that digit in decimal.
        B) num >>= 1 shifts the digits of the number to the right by one. So we can check the next digit. Later count
        is increased by one because now we are working with a bigger digit.
        C) If the original number is 0 then we are finished. Because in the end every digit will be shifted to the
        right and we will have 0.
"""

def complementBitwise(num):
    count = 0
    comp = 0
    while True:
        if num == 0:
            break
        if not num & 1:
              comp = comp + 2**count
        num >>= 1
        count += 1
    print(comp)

complementBitwise(10)
complementBitwise(5)
complementBitwise(190)