n = int(input())    #컴퓨터의 수
m = int(input())    #연결된 컴퓨터 쌍의 수    #간선의 개수

graph = [[] for _ in range(n+1)]

def dfs(c):
    global answer         #함수 안에서 ans의 개수 카운트 해주기 위해서

    answer += 1           #감염된 컴퓨터 수 하나 늘었음 , 즉 1에 연결된 정점마다 카운트
    visited[c] = 1        #방문했으니까 1로 표시

    for n in graph[c]:           #근데, 연결된 노드들이 있으니까 돌면서 연결된 거 있는지 없는지 볼거임
        if not visited[n]:       #즉 visited[n]에서
            dfs(n)


for _ in range(m):                    #연결된 컴퓨터 쌍의 수만큼 반복 => 연결된 쌍의 수 만큼 이동해서 바이러스 걸렸는지 봐야됨
    x, y = map(int, input().split())
    graph[x].append(y)         #graph[1]에 2를 넣어줌  graph[2]에 3을 넣어줌   이렇게 쭉쭉쭉 graph에 넣어줌
    graph[y].append(x)         #graph[2]에 1을 넣어줌  graph[3]에 2를 넣어줌



answer = 0                        #감염된 pc 개수
visited = [0] * (n + 1)            # 방문처리 할 visited 배열 생성
dfs(1)                            #start point 1 => 문제에서 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수

print(answer - 1)    #1번 컴퓨터 빼줌
