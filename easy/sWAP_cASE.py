"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""
def upper_lower(a):
    if a.isupper():
        return a.lower()
    else:
        return a.upper()
    
def swap_case(s):
    str_list = list(map(upper_lower, s))
    return "".join(str_list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)