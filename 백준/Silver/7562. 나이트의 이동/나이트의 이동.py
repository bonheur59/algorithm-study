from sys import stdin
from collections import deque

t = int(stdin.readline())

#나이트 이동 경로
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]


def bfs(x, y, gx, gy):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 1    #방문처리

    while queue:
        pop_x, pop_y = queue.popleft()

        if pop_x == gx and pop_y == gy:
            print(visited[pop_x][pop_y] - 1)
            break

        for i in range(8):     #방향 탐색
            nx = pop_x + dx[i]
            ny = pop_y + dy[i]

            if 0<=nx<l and 0<=ny<l :
                if visited[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[pop_x][pop_y] + 1


for _ in range(t):
    l = int(stdin.readline())
    visited = [[0] * l for i in range(l)]

    start_x, start_y = map(int, stdin.readline().split())   #현재 위치
    goal_x, goal_y = map(int, stdin.readline().split())     #목표 위치

    if start_x == goal_x and start_y == goal_y: # 타겟 좌표와 같은 좌표면 0
        print(0)
    else:
        bfs(start_x, start_y, goal_x, goal_y)
