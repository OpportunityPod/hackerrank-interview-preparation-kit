
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
