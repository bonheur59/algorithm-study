import sys

input = sys.stdin.readline

n = int(input())

list = []
for i in range(n):
    age, name = map(str, input().split())
    list.append((int(age), i, name))


list.sort()

for i in range(n):
    print(list[i][0] , end=' ')
    print(list[i][-1])
