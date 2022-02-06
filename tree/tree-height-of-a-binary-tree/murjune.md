
재귀호출을 통해 루트 노드를 시작점 leaf노드를 끝점으로 잡고, 자식방향으로 내려가면서, 높이(cnt)를 갱신해준다.  

```python
def height(root):
    
    if root == None:
        return -1
    
    left = height(root.left)
    right = height(root.right)
    cnt = max(left, right) + 1
    
    return cnt
```
