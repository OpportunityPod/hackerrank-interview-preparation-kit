# 풀이 - 완전탐색 + 백트래킹
- 1. stack이 비었는지 확인(모두 비었으면 정답)  
- 2. stack.pop() : stack으로부터 넣을 단어 가져오기  
- 3. PossibleLocation() :단어를 넣을 후보 (x,y,축) 구하기 (축: 수평(right), 수직(down))  
- 4. solve :다음 단어로 1~3번 재귀적으로 수행하기  
- 5. back :단어 넣었던 공간 '-'로 되돌리기한 후 3번 수행. 
- 6. stack.append(word) : 단어 다시 stack에 넣기

```python


# print graph
def print_sol(graph):
    for row in graph:
        print(''.join(row))
# Search possibleLoc
def possibleLoc(word):
    posLoc = []
    n = len(word)

    # 1. down
    for i in range(10):
        for j in range(10-n + 1):
            isPos = True ;
            for k in range(n):
                if graph[i][j+k] == '-' or  graph[i][j+k] == word[k]:
                    continue
                isPos  = False;
                break
            if isPos:
                posLoc.append((i,j,0)) # 0 is down

    # 2. right
    for i in range(10-n + 1):
        for j in range(10):
            isPos = True ;
            for k in range(n):
                if graph[i+k][j] == '-' or  graph[i+k][j] == word[k]:
                    continue
                isPos  = False;
                break
            if isPos:
                posLoc.append((i,j,1)) # 0 is right

    return posLoc

# go
def go(word,loc):
    i,j, situation = loc;

    if situation == 0: # down
        for k in range(len(word)):
            graph[i][j+k] = word[k];
    else: # right
        for k in range(len(word)):
            graph[i+k][j] = word[k];

# back
def back(word,loc):
    i, j, situation = loc;

    if situation == 0:  # down
        for k in range(len(word)):
            graph[i][j + k] = '-';
    else:  # right
        for k in range(len(word)):
            graph[i + k][j] = '-';

def solve(graph, stack):
    global isSolved ;
    # 0. isSolved?

    # 1. stack is empty?
    if not stack :
        if isSolved:
            return
        print_sol(graph) ; # print graph
        isSolved = True ;# finish :D
        return

    # 2. pop from stack
    word = stack.pop();

    # 3. Search possibleLoc
    posLoc = possibleLoc(word);

    # (brute-force)
    for pos in posLoc:
        # 4. go
        go(word,pos)
        # 5. recursion
        solve(graph,stack)
        # 6. back
        back(word,pos)

    # 7. append word
    stack.append(word)

# solve
graph = [list(input()) for _ in range(10)]

stackWords = list(input() .split(";")) 
isSolved = False
solve(graph, stackWords)
```
