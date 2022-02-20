
1. 
``` python

def fibonacci(n):
    global result
    if n <= 1: 
        result[n] = n
        return n
    result[n] = result[n-1] + result[n-2]
    return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input())
result = [0] * (n+1)
print(fibonacci(n))

```

2. 
``` python
print(round((((1+(5**0.5))/2)**int(input()))/(5**0.5)))
```

3.
``` python
# from functools import lru_cache 


# @lru_cache(30) 
# def fibonacci(n):
#     return fibonacci(n-1) + fibonacci(n-2) if n>2 else 1

```

4.

``` python
def fibonacci(n):
    result = [0,1] + [0]*(n)
    for i in range(2, n+1):
        result[i] = result[i-1] + result[i-2]
    return result[n]

n = int(input())
print(fibonacci(n))




```
