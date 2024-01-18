import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    item = [list(map(int, input().strip().split())) for _ in range(n)]
    item.sort()

    count = 1
    standard = item[0][1]
    for i in range(1, len(item)):
        if item[i][1] < standard:
            count += 1
            standard = item[i][1]
    print(count)



# 겹치지 않고, 오름차순이든 내림차순이든
# a와 b를 비교했을 때, a가 더 크면 b는 더 작아야 함
# 5 5  => x
# 4 1   => 0
# 3 2
# 2 3
# 1 4
#
# 7 3       => x
# 6 1
# 5 7       => x
# 4 2
# 3 6       => x
# 2 5       => x
# 1 4               =>
