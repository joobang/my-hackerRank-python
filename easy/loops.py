#The provided code stub reads and integer, n , from STDIN. For all non-negative integers i < n, print i2 .

if __name__ == '__main__':
    n = int(input())
    def solution(n: int):
        for i in range(n):
            print(i*i)
    
    solution(n)