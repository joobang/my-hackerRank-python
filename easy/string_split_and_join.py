"""
input : this is a string
output : this-is-a-string
"""
def split_and_join(line):
    # write your code here
    split_str = line.split()
    return "-".join(split_str)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)