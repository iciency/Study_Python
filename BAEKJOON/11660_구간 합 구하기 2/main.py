import sys

input = sys.stdin.readline
N, M = map(int,input().split())

array = []
for i in range(N):
    array.append(list(map(int,input().split())))

# 누적합

# 길이 == 입력의 길이 + 1
prefix_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]

#초기화
for i in range(N):
    for j in range(N):
        prefix_sum[i+1][j+1] = prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j] + array[i][j]


#질문의 수
for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    result = prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1]
    print(result)
