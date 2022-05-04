#!/usr/bin/python3
def roman_to_int(roman_string):
    s = roman_string
    val = 0
    r_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if s is None and type(s) != str:
        return val
    for i in range(len(s)):
        if i > 0 and r_val[s[i]] > r_val[s[i - 1]]:
            val += r_val[s[i]] - 2 * r_val[s[i - 1]]
        else:
            val += r_val[s[i]]
    return val
