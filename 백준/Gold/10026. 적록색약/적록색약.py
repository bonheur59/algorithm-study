import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input())
graph1 = []
graph2 = []
visited1 = [[0] * n for _ in range(n)]
visited2 =  [[0] * n for _ in range(n)]

#색깔 정보 받기
for _ in range(n):
    s = input()
    graph1.append(list(s))
    graph2.append(list(s.replace('G','R')))


def dfs(graph, visited,  x, y):
    visited[x][y] = 1
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 좌표의 범위를 벗어나지 않도록 함
        if (0 <= nx < n) and (0 <= ny < n) and (graph[nx][ny] == graph[x][y]) and not visited[nx][ny]:
            dfs(graph, visited, nx, ny)


#좌표 돌면서 아직 방문하지 않은 노드를 찾아 DFS 실행
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            dfs(graph1, visited1, i, j)
            cnt1 += 1     #cnt는 구역의 수
print(cnt1, end=' ')


#적록색약 일 때
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            dfs(graph2, visited2, i, j)
            cnt2 += 1
print(cnt2)