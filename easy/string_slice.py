"""
string slice
string = "abcd"
string[start_index:endindex] 
ex) string[:1] --> "a"
    string[2:] --> "cd"
"""
def mutate_string(string, position, character):
    new_str = string[:position] + character + string[position+1:]
    return new_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)