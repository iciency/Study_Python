import sys
input = sys.stdin.readline

# N = int(input()) #재료의 수
# M = int(input()) #갑옷을 만드는데 필요한 재료의 수
# Array = list(map(int,input().split())) # 갑옷 재료 리스트
N = 6
M = 9
Array = [1,3,5,7,1,4,2]
start = 0
end = N-1
count = 0 #갑옷을 만들 수 있는 수

Array.sort()
while True:
    if start >= end:
        print(count)
        break
    if Array[start] + Array[end] < M:
        start += 1
    elif Array[start] + Array[end] > M:
        end -= 1
    else:
        count +=1
        end -= 1
        start += 1