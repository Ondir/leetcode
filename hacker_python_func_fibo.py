from functools import lru_cache

cube = lambda x: x**3 # complete the lambda function

@lru_cache
def fibonacci(n):
    lis = [0, 1]
    for i in range(2,n):
         lis.append(lis[i-2] + lis[i-1])
    return (lis[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))