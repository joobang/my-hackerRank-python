"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
The first line of input contains the original string. The next line contains the substring.
Output the integer number indicating the total number of occurrences of the substring in the original string.
"""
def count_substring(string, sub_string):
    
    output = 0
    i = 0
    sub_str_len = len(sub_string)
    isEnd = False
    while not isEnd:
        if string.find(sub_string,i) >= 0:
            output += 1
            i = string.find(sub_string,i)+1
        else:
            isEnd = True
    return output

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)