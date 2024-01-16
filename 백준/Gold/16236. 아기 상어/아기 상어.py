from collections import deque
import sys

input = sys.stdin.readline

'''
활용 알고리즘 : BFS
1. 아기 상어의 초기 위치를 찾음
2. 어떤 물고기들을 먹을 수 있는지 체크 -> BFS :먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기 먹음
3. 상어가 해당 물고기를 먹으러 이동
4. while문을 이용하여 BFS 반복 수행

=> 자신의 크기와 같은 수의 물고기를 먹을때 마다 아기상어의 크기 증가
=> 더이상 먹을 물고기가 없는 경우(엄마상어에게 도움 요청) => 종료 조건
'''

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

shark_size = 2     #초기 상어의 크기

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j, shark_size):
    visited = [[0] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    eatable = []          #먹을 수 있는 물고기 리스트

    q = deque()
    q.append((i, j))

    if not visited[i][j]:
        visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1

                    #이동이 가능할 때
                    if graph[nx][ny] <= shark_size:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y] + 1

                        #이동이 가능하고, 물고기를 먹을 수 있을 때 => 물고기의 크기가 아기 상어보다 작을 때
                        if graph[nx][ny] != 0 and graph[nx][ny] < shark_size:
                            eatable.append((nx, ny, distance[nx][ny]))

    return sorted(eatable, key=lambda x : ((x[2], x[0], x[1])))  #거리, x, y순으로 오름차순



time = 0            #시간
eat_cnt = 0         #먹은 횟수

#1. 아기상어의 초기 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:    #만약 아기상어의 위치 발견시
            shark_i, shark_j = i, j      #상어의 현재 위치 저장
            graph[i][j] = 0             #0으로 초기화
            break


#2. 먹을 수 있는 물고기들 체크하기
while True:
    fish_info = bfs(shark_i, shark_j, shark_size)

    if not fish_info:      #먹을 물고기가 없는 경우
        break


    nx, ny, d = fish_info[0]    #3. #가장 가까운 거리의 물고기를 꺼내 먹음
    time += d
    eat_cnt += 1

    #4. 자신의 크기와 같은 수의 물고기를 먹을 때 마다 아기상어의 크기 증가
    if eat_cnt == shark_size:
         shark_size += 1
         eat_cnt = 0

    #상어 좌표를 먹은 물고기 좌표로 옮겨줌
    graph[shark_i][shark_j] = 0
    shark_i, shark_j = nx, ny

print(time)