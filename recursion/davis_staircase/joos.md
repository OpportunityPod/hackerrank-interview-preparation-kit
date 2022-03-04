
# solution 1 
``` python
cache = dict()
def stepPerms(n):
    if n <= 2:return n
    if n == 3:return 4
    if n not in cache:
        cache[n] = stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3)
    return cache[n]
```

# solution 2 
``` python
def stepPerms(n):
    m=1
    p=2
    q=4

    for i in range(1, n):
        tmp = m+p+q
        m = p
        p = q
        q= tmp
        
    return m
```
