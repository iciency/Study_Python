import sys
_input = sys.stdin.readline
N, M = map(int,_input().split())

A = list(map(int,_input().split()))

S = [0] * (len(A) + 1)

for i in range(N):
    S[i+1] = S[i] + A[i]

for _ in range(M):
    i,j = map(int,_input().split())
    print(S[j]- S[i-1])