from collections import deque
import sys


n,m,v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]


dfs_visited = [0] * (n+1)       #방문했는지 알아보는 리스트
bfs_visited = [0] * (n+1)

dfs_result = []
def dfs(graph, v):

    global dfs_visited

    dfs_result.append(v)      #startpoint부터 visited에 append 해줌
    dfs_visited[v] = 1

    #탐색 조건
    for i in graph[v]:
        if not dfs_visited[i]:          #방문한 노드가 아니라면 계속해서 탐색
            dfs(graph, i)

bfs_result = []
def bfs(graph, v):
    queue = []             #큐를 생성

    global bfs_result

    queue.append(v)
    bfs_visited[v] = 1

    while queue:                    #큐가 있다면
        value = queue.pop(0)        #popleft()
        bfs_result.append(value)    #방문한 노드(pop한 노드)를 bfs_result에 추가

        for i in graph[value]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i] = 1   #visited에 방문 표시


for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)            #그래프가 서로 연결되어 있기 때문
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


dfs(graph, v)    # 1, 2
bfs(graph, v)
print(*dfs_result, "")
print(*bfs_result, "")
