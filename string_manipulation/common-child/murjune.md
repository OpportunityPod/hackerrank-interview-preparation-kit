# 풀이 1 : pypy3으로 제출해야 정답처리됩니다 :D 
- 시간복잡도 : O(N^2), 공간복잡도 : O(N^2)
```python
def commonChild(s1, s2):
    # Write your code here
    d = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(1, n): # ACAYKP
        for j in range(1, m): # CAPCAK
            if s1[i] == s2[j]:
                d[i][j] = d[i-1][j-1] + 1
            elif s1[i] != s2[j]:
                d[i][j] = max(d[i][j-1], d[i-1][j])
    
    return d[n-1][m-1]
```

# 풀이 2
- 시간복잡도 : O(N^2), 공간복잡도 : O(N)
```python
def commonChild(s1, s2):
    # Write your code here
    n, m = len(s1), len(s2)
    d = [0] * (5000)

    for i in range(n):
        cnt = 0
        for j in range(m):
            
            if cnt < d[j]:
                cnt = d[j]

            elif s1[i] == s2[j]:
                d[j] = cnt + 1
    return max(d)
```
