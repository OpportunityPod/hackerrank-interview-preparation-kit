```python
from collections import deque

def decodeHuff(root, s):
    # step 1
    s = list(s)
    q = deque(s)
    now = root
    while q:
        # step 2
        if not now.left and not now.right:
            print(now.data, end="")
            now = root  # init
            
        v = q.popleft()
        
        # step 3
        if v == '0':
            now = now.left
        elif v == '1':
            now = now.right 
            
    # step 4
    if not now.left and not now.right:
        print(now.data, end="")
```  
문제 설명은 생략하겠습니다~  

- step 1: s 를 list타입으로 타입변환 후, deque 자료구조에 넣어줍니다.(FIFO을 사용하기 위해)  

- step 2: 만약, now(현재 노드)가 자식이없는 leaf노드라면, leaf노드값을 출력해준 후, now를 Tree의 root로 초기화시켜줍니다.  

- step 3: 문제에 주어진 조건대로, 암호가 '0'이면 왼쪽자식, '1'이면 오른쪽 자식으로 이동  

- step 4: q에 들어있는 마지막 원소를 처리해주기 위해, step2를 한 번 더 수행해줍니다.  

