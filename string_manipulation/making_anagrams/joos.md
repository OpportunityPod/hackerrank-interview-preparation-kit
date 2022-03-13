

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
