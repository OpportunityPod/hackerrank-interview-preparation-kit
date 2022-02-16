
def bfs(s,target):

    q = deque([s])

    while q:
        now = q.popleft()
        if now != s and color[now] == target:
            print(visited[now])
            return

        for next in graph[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                q.append(next)

    print(-1)

from  collections import deque
n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a , b = a-1 , b - 1
    graph[a].append(b)
    graph[b].append(a)

visited = [-1]*n
color = list(map(int,input().split()))
s = int(input()) - 1
target = color[s]
visited[s] = 0
bfs(s,target)
