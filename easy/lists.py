"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
"""
if __name__ == '__main__':
    N = int(input())
    list_arr = []
    for i in range(N):
        input_str = input()
        input_split = input_str.split(' ')
        #print(input_split)
        if input_split[0] == 'insert':
            list_arr.insert(int(input_split[1]),int(input_split[2]))
        elif input_split[0] == 'print':
            print(list_arr)
        elif input_split[0] == 'remove':
            list_arr.remove(int(input_split[1]))
        elif input_split[0] == 'sort':
            list_arr.sort()
        elif input_split[0] == 'pop':
            list_arr.pop()
        elif input_split[0] == 'reverse':
            list_arr.reverse()
        elif input_split[0] == 'append':
            list_arr.append(int(input_split[1]))