## 분할 정복 (Divide and Conquer)

<br />그대로 해결할 수 없는 문제를 작은 문제로 분할하여 문제를 해결하는 알고리즘. 자연스럽게 재귀의 형태로 구현.

다른 재귀 알고리즘과 구별되는 차이점은 보통 2개 이상의 하위 문제로 나누어 처리.

<br />**Divide** : 큰 문제를 작은 문제로 분할하는 것을 의미

**Conquer** : 작은 문제의 답으로 큰 문제의 답을 구하는 것

![image](https://user-images.githubusercontent.com/39346980/154774095-7e170413-d06c-4d68-9fad-55498f3c1983.png)


### 합병 정렬 (Merge Sort)
 
<br />**1. Top-down Approach (하향식)**
<br />
- 비정렬 배열을 여러 하위 배열로 나누기 (Divide)

- 하위 배열을 재귀적으로 정렬 (Conquer)

- 정렬된 하위 배열을 병합하여 새로운 정렬된 배열 생성 (Combine)<br />

![image](https://user-images.githubusercontent.com/39346980/154774301-ae96488d-7943-4353-bd60-a2c2a142fe6f.png)
![image](https://user-images.githubusercontent.com/39346980/154774312-8a2a46f7-8534-4fa3-b987-16b221e82c11.png)


**2. Bottom-up Approach (상향식)**

<br />비정렬 배열을 처음부터 하위 배열로 나누기. 하위 배열끼리 이미 정렬. 그 다음 1개의 정렬된 배열로 남을때까지 2개의 하위 배열을 병합.
<br /><br />

![image](https://user-images.githubusercontent.com/39346980/154774322-44d3fff4-8a77-4e3c-9dbf-d7ecde25c0db.png)

시간복잡도 **O(nlogn)** : n은 input 배열의 길이.


n/2, n/2 (2개)

n/4, n/4, n/4, n/4 (4개)

n/8, n/8, n/8, n/8, n/8, n/8, n/8, n/8 (8개)

분할을 할때마다 1/2씩 감소하므로 logn 만큼 반복. 각 분할별로 merge.

 
<br />퀵 정렬(Quick Sort)과 합병 정렬(Merge Sort)은 분할정복(Divide and Conquer)으로 정렬을 해나간다는 공통점.

퀵 정렬은 최악의 경우 시간복잡도 O(n^2), 합병 정렬은 최악의 경우에도 시간복잡도 O(nlogn).
<br /><br /><br />

### 퀵 정렬 (Quick Sort)
<br />pivot을 기준으로 작거나 같은 값을 지닌 데이터는 앞으로, 큰 값을 지닌 데이터는 뒤로 가도록 하여, 작은 값을 갖는 데이터와 큰 값을 갖는 데이터로 분리해가며 정렬하는 방법.

분리하는 과정을 Partitioning 이라고 한다.

![image](https://user-images.githubusercontent.com/39346980/154774354-f7e94a9e-a93c-4807-a7de-23c5616aba26.png)

 

1. 입력받은 배열에서 기준이 되는 값인 pivot을 설정

2. pivot을 기준으로 pivot 보다 작은 값은 왼쪽, 큰 값은 오른쪽에 옮겨진다.

3. 왼쪽과 오른쪽 배열의 크기가 1이 될 때까지 1, 2번 반복<br /><br />

![image](https://user-images.githubusercontent.com/39346980/154774371-e836968b-5c98-48ff-b032-9e5fa225fe47.png)


시간복잡도 Best case **O(nlogn)**, Worst case **O(n^2)**

 

**O(n^2)** : 최악의 경우. (걸리는 시간 n) * (반복해야할 횟수 n)

pivot을 설정했지만, 나머지 값들이 pivot의 왼쪽이나 오른쪽 한쪽으로 몰린 경우.

![image](https://user-images.githubusercontent.com/39346980/154774407-5cb58918-58d1-4cfd-a7cf-5b882bb8889d.png)

<br />

**O(nlogn)** : 최선의 경우. (걸리는 시간 n) * (반복해야할 횟수 logn)

각 하위 배열이 input 배열의 크기의 절반으로 나누어지는 경우.

![image](https://user-images.githubusercontent.com/39346980/154774429-f9eccda4-347a-4717-b617-fbe009eba2f1.png)

<br />

## 백트래킹 (Backtracking)

 ![image](https://user-images.githubusercontent.com/39346980/154774451-cf06ecbb-0506-4493-bd27-f44e2cfb3727.png)


<br />해를 찾아가는 도중, 지금의 경로에 해가 될 것 같지 않으면 그 경로를 더 이상 가지않고 되돌아가서 다시 해를 찾는 기법.
가지치기(Pruning)를 이용해 불필요한 탐색을 줄이는 알고리즘. 즉, 반복문의 횟수를 줄일 수 있으므로 효율적.

 

<br />일반적으로 불필요한 경로를 조기에 차단할 수 있게되어 경우의 수가 줄어들지만, 만약 N!의 경우의 수를 가진 문제에서 최악의 경우에는 여전히 지수함수 시간(Polynomial)을 필요로 하므로, **가지치기를 얼마나 잘하느냐에 따라 효율성**이 결정되게 된다.

 

<br />주로 문제 풀이에서 **DFS(깊이우선탐색) 등으로 모든 경우의 수를 탐색하는 과정에서, 조건문 등을 걸어 답이 절대 될 수 없는 상황을 정의하고, 그러한 상황일 경우에는 탐색을 중지시킨 뒤 그 이전으로 돌아가서 다시 다른 경우를 탐색하게끔** 구현할 수 있다.

<br />

 ![image](https://user-images.githubusercontent.com/39346980/154774491-7fdfbd2d-3188-4da9-8038-10602e88c07b.png)


### 유망성(Promising) 판단
 

<br />어떤 노드의 유망성, 즉 **해가 될 만한지 판단한 후 유망하지 않다고 결정되면, 그 노드의 이전(부모)로 돌아가(Backtracking)** 다음 자식 노드로 간다.


<br />문제. Backtracking을 적용하여 트리에서 단어 **AIM** 탐색<br />

![image](https://user-images.githubusercontent.com/39346980/154774521-47e9b35d-8efb-4174-a628-7e35f0d89457.png)

![image](https://user-images.githubusercontent.com/39346980/154774528-37c914f7-3d06-48d7-af47-230d1b07c115.png)

