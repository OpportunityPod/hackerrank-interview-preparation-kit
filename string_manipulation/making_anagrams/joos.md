# 1. 

``` python
from collections import Counter

def makeAnagram(a, b):
    a_counter = Counter(a)
    b_counter = Counter(b)
    overlap_character = a_counter.keys() & b_counter.keys()
    
    result = []
    for i in overlap_character:
        result.append(
            min(a_counter[i], b_counter[i])
        )

    
    return len(a) + len(b) - 2*(sum(result))
```

# 2. 
``` python

def makeAnagram(a, b):
    characters = [0] * 26  # 문자열 a을 구성하는 알파벳 개수 담을 테이블
    for c in a:
        characters[ord(c) - 97] += 1
    for c in b:
        characters[ord(c) - 97] -= 1

    ans = 0

    for i in range(26):
        ans += abs(characters[i])  # 알파벳의 개수가 일치하지 않으면 그 차를 ans에 더한다

    return ans
```
