import sys
input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))
list.sort()

min = 0

for i in range(len(list)):
    min += sum(list[0:i+1])

print(min)

