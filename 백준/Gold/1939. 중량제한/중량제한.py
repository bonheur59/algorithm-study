import sys
from collections import deque
 
def bfs(weight):
    visited = [False for _ in range(N)]
    visited[start] = True
    Q = deque()
    Q.append(start)
    while Q:
        current = Q.popleft()
        if current == end:
            return True
        for next_weight,next in G[current]:
            if not visited[next] and next_weight >=weight:
                visited[next] = True
                Q.append(next)
    return False
 
input = sys.stdin.readline
N,M = map(int,input().split())
G= [[] for _ in range(N)]
 
for _ in range(M):
    a,b,c  =map(int,input().split())
    a,b = a-1,b-1
    G[a].append((c,b))
    G[b].append((c,a))
start,end = map(int,input().split())
start,end = start-1,end-1
 
s,e = 1, 1_000_000_000
ans = s
while s<=e:
    m = (s+e)//2
    if bfs(m):
        ans = m
        s = m+1
    else:
        e = m -1
print(ans)