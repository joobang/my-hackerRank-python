"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
The first line contains n. The second line contains an array A[]  of  n integers each separated by a space.
2 <= n <= 10 
-100 <= A[i] <= 100

"""
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #result = list(set(list(arr)))
    #result.sort(reverse=True)
    #print(result[1])
    
    list_arr = list(arr)
    list_arr.sort(reverse=True)
    first, second = -100,-100
    for i in list_arr:
        if i >= first:
            first = i
        elif i > second:
            second = i
    print(second)