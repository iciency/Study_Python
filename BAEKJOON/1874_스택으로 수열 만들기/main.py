import sys

input = sys.stdin.readline

N = int(input())
stack = [] 
start = 1
result = []

for _ in range(N):
    end = int(input())
    while start <= end:
        stack.append(start) 
        result.append('+')
        start += 1
    if stack[-1] == end : 
        stack.pop() 
        result.append('-')
    else: 
        print("NO") 
        exit()

for i in result:
    print(i)