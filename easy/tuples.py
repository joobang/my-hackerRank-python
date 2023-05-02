# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
Given an integer, N , and N space-separated integers as input, create a tuple, t , of those n integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

The first line contains an integer, N , denoting the number of elements in the tuple.
The second line contains N space-separated integers describing the elements in tuple t.
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuple_tmp = tuple(integer_list)
    print(hash(tuple_tmp))
