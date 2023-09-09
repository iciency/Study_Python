import sys

input = sys.stdin.readline

N,M = map(int,input().split())

A = []

for _ in range(N):
    A.append(list(map(int,input().split())))


D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]


for i in range(N):
    for j in range(N):
        D[i+1][j+1]= D[i+1][j] + D[i][j+1] + A[i][j] - D[i][j]
        
for _ in range(M):
    x1,y1,x2,y2 = map(int,(input().split()))
    print(D[x2][y2] - D[x2][y1-1] - D[x1-1][y2] + D[x1-1][y1-1])