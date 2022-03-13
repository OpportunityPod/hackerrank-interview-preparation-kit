# 1
```python
# 시간복잡도 : O(N)
def makeAnagram(a, b):
    d1 = [0]*26; # 문자열 a을 구성하는 알파벳 개수 담을 테이블
    d2 = [0]*26; # 문자열 b을 구성하는 알파벳 개수 담을 테이블
    for c in a:
        d1[ord(c)-97] += 1; 

    for c in b:
        d2[ord(c)-97] += 1;
    
    ans = 0;

    for i in range(26):
        ans += abs(d1[i]-d2[i]); # 알파벳의 개수가 일치하지 않으면 그 차를 ans에 더한다
    
    return ans;
```
# 2
```python
def makeAnagram(a, b):
    from collections import Counter
    d = Counter(a)
    d2 =Counter(b)
    
    tmp = d&d2
    tmp2 = d|d2
    tmp2.subtract(tmp)
    
    ans = 0
    for val in tmp2.values():
        ans += val;
    return ans
```
