3가지 방법으로 문제를 풀었습니다.  
자세한 설명은 다음 링크를 참조해 주세요:)  
[ISBST by murjune](https://murjune.github.io/IsBST/). 

# 방법 1. 
BST를 inorder(L-N-R) 순회하였을 때, 그 결과 값은 모든 노드값을 오름차순한 결과값과 같습니다.
따라서, inorder 순회를 하며, 배열에 노드값을 순회에 따라 넣어주고, 그 배열이 오름차순이면 True, 아니면 False
```python
def Inorder(root,arr): # 인오더 함수
    if root is None:
        return 
    
    if root.left:
        Inorder(root.left,arr)
    
    arr.append(root.data)
    
    if root.right:
        Inorder(root.right,arr)
    
    return arr


def checkBST(root):
    arr= []
    arr = Inorder(root,arr) 
    # 해당 arr가 오름차순인지 판별
    for i in range(1,len(arr)-1):
        if arr[i] <= arr[i-1]: # 문제에서, 중복 허용 x (중복 허용하면 <)
            return False
    return True
```
# 방법 2  
위에 1번 판별방법에서, N크기의 arr를 생성한 점을 보완한 풀이이며, inorder 순회를 활용한 점은 같습니다.
어차피 우리가 필요한건, 현재 값과 그 전의 값을 비교하는 것이므로,
pre라는 변수를 하나 만들어 트리를 순회하면서 노드값과 비교하며, pre를 갱신해줍니다.  ->(공간복잡도를 효율적으로 사용가능)

```python
pre = 0
flag = True # pre >= node값 인 경우 False를 담기 위한 boolen 변수
def checkBST(root):
    global flag
    Inorder(root)
    return flag


def Inorder(root):
    global flag,pre
    
    if flag == False:
        return 
    if root is None:
        return
    
    # L
    if root.left:
        Inorder(root.left)
    # N
    if not pre: # pre가 비었으면, 노드값 할당
        pre = root.data
    elif pre : 
        if pre < root.data: # 오름차순 check -> pre값 갱신
            pre = root.data
        else: # 오름 차순 x -> flag False
            flag = False
    # R
    if root.right:
        Inorder(root.right)
```
# 방법 3  
3번째 BST 판별 방법은 root 노드에서 자식 방향으로 내려가면서 해당 node가 가질 수 있는 영역(범위)를 제한하는 방법입니다.  
```python


import sys



def checkBST(root,MIN_VAL= -sys.maxsize, MAX_VAL= sys.maxsize): # boolen

    # root x
    if root is None: return True

    # root o
    if root.data <= MIN_VAL or MAX_VAL <= root.data: return False

    if not checkBST(root.left, MIN_VAL, root.data) or not checkBST(root.right, root.data, MAX_VAL):
        return False
    
    return True
```
