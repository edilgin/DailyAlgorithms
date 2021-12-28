"""
Q: Given a number return its binary complement
"""
def turnBinary(num):
    binary = []
    # find the binary of the decimal
    while num != 0:
        binary.append(num % 2)
        num = num // 2
    # reverse the binary list
    for i in range(len(binary)//2):
        tmp = binary[i]
        binary[i] = binary[-i-1]
        binary[-i-1] = tmp
    return binary

def complement(num):
    # get the binary representation of the number
    binary = turnBinary(num)
    print("binary: ", binary)
    # if 1 is encountered turn it to 0 if 0 is encountered turn it to 1
    for i in range(len(binary)):
        if binary[i] == 0:
            binary[i] = 1
        else:
            binary[i] = 0
    print("complement: ", binary)

# test the algorithm with various values
complement(5)
complement(10)
complement(18)