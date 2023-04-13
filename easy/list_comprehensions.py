"""

0<= i <= x
0<= j <= y
0<= k <= z
x,y,z,n = 1,1,1,2
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1],[1, 0, 1],[1, 1, 0],[1, 1, 1]]
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    output = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    #result = [arr for arr in output if sum(arr) != n]
    #print(result)
    print(output)