import sys
input = sys.stdin.readline

n = int(input())   #도시의 수
distance = list(map(int, input().strip().split())) #거리
price = list(map(int, input().strip().split()))   #가격

result = 0
min_price = price[0]     #처음에는 무조건 주유를 해야 함

for i in range(0, n-1):
    if price[i] < min_price:   #만약 현재 가격이 min_price보다 적으면
        min_price = price[i]   #현재 가격을 min_price로
    result += min_price * distance[i]

print(result)
