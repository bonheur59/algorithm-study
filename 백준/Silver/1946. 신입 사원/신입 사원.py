import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    rank = sorted([list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]) # 서류를 기준으로 정렬
    cnt = 1
    second_rank = rank[0][1]
    for i in range(1,N):
        if rank[i][1] < second_rank: # 면접 순위가 이전사람들보다 높으면
            cnt += 1 # 횟수 증가
            second_rank = rank[i][1]
    print(cnt)