import sys
input = sys.stdin.readline

N, M = 5, 3
# N, M = map(int,input().split())
# array = list(map(int,input().split()))

array = [1,2,3,1,2]
S = [0] * (len(array) + 1)
C = [0] * M

for i in range(N):
    S[i+1] = array[i] + S[i] #합 배열 최기화
    C[S[i+1] % M] += 1 #겹치는 인덱스 카운트
        
cnt = C[0]  # 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수

for i in C:
    cnt += i * (i - 1) // 2

print(cnt)