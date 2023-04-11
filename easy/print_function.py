"""
The included code stub will read an integer, n, from STDIN.
Example
n=5
Print the string 12345.
"""


if __name__ == '__main__':
    n = int(input())
    def printN(n: int):
        temp_str = ''
        for i in range(n):
            temp_str += str(i+1)
        print(temp_str)
    printN(n)