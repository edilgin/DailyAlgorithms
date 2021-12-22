def romanConv(roman_value):
    count = 0
    dct = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400,"CM":900}
    dct2= {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    for i in dct:
        amount = roman_value.count(i)
        count += amount * dct[i]
        roman_value = roman_value.replace(i, "")
    for i in roman_value:
        count += dct2[i]
    return count


roman_val = "III"
print(romanConv(roman_val))
roman_val = "LVIII"
print(romanConv(roman_val))
roman_val = "MCMXCIV"
print(romanConv(roman_val))
