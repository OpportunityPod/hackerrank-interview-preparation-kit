from collections import deque
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = [[] for _ in range(n)]
    
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        x-=1
        y-=1
        graph[x].append(y)
        graph[y].append(x)
        
    s = int(input()) - 1 
    visitied = [-1] * n # 간선 비용 모두 -1로 시작
    visitied[s] = 0 # 시작점 dist = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for next_c in graph[x]:
            if visitied[next_c] == -1: # 만약 방문 한적 없으면
                visitied[next_c] = visitied[x] + 6 # 현재 도시의 간선 + 간선 비용(6)
                q.append(next_c) # q에 next 노드 넣기
    
    ans = []
    for i in range(n):
        if i == s:
            continue
        ans.append(visitied[i])
    
    print(' '.join(map(str, ans)))
        
