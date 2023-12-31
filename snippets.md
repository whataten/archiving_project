# Python Code Snippets
### 1. String manipulation (~165p)
> 2차원 배열 ['1, B', '2, A']에서 **두 번째 요소(알파벳)순으로 정렬**
> 
> ``` python
> strs = ['1, B', '2, A']
> strs.sort(key=lambda x: (x.split()[1:], x.split()[:1]))
> ```

> 문자열에 **숫자와 문자만 남기기**  
> 
> ``` python
> strs = 'A man, a plan, a canal: Panama'
> for s in strs:
>     if s.isalnum():
>         pass
> ```

> **리스트로 단어 골라내기**
> 
> ```python
> strs = ['a', 'b', 'c', 'd']
> banned = ['a']
> result = [word for word in strs if word not in banned]
> ```

> 리스트 요소 중 **최빈 값, 빈도 찾기**
> 
> ```python
> import collections
> strs = ['a', 'a', 'b', 'c', 'd']
> value = collections.Counter(strs).most_common()[0][0]
> count = collections.Counter(strs).most_common()[0][1]
> ```
### 2. List manipulation (~198p)
> **원본 리스트 정렬**, **원본 리스트 유지하며 정렬**
> 
> ```python
> strs = ['1', '3', '2']
> strs.sort()
> sorted_strs = sorted(strs)
> ```

> 리스트 **중복 값 제거**
> ```python
> strs = ['1', '3', '3']
> list(set(strs))
> ```

> **최댓값 최솟값** 지정
> 
> ```python
> import sys
> mx = -sys.maxsize
> mn = sys.maxsize
> mx = float('inf')
> mn = float('-inf')
> ```
### 3. Linked list manipulation (~239p)
> **데크**
> 
> ```python
> import collections
> strs = collections.deque()
> strs.append('a')
> strs.appendleft('a')
> strs.pop()
> strs.popleft()
> ```

> **리스트를 문자열로**
> 
> ```python
> strs = ['a', 'b', 'c']
> ''.join(word for word in strs)
> ''.join(strs)
> ```

> **스왑**
> 
> ```python
> a = 1
> b = 2
> a, b = b, a
> ```
### 4. Stack, Queue manipulation (~265p)
> 리스트 **기본값** 설정
> 
> ```python
> T = [1, 2, 3, 4]
> strs = ['기본값'] * len(T)
> ```

> **우선순위 큐**
> 
> ```python
> import heapq
> heap = []
> heapq.heappush(heap, (1, 'b'))
> heapq.heappop(heap)
> ```

> **최대 힙** 구현
> 
> ```python
> import heapq
> heap = [1, 3, 5, 7, 9]
> max_heap = []
> for item in heap:
>     heapq.heappush(max_heap, (-item, item))
> ```
### 5. Hash table manipulation (~313p)
> **딕셔너리로 개수 확인**
> 
> ```python
> dic = {}
> strs = ['a', 'a', 'b']
> for word in strs:
>     if word in dic:
>         dic[word] += 1
>     else:
>         dic[word] = 1
> ```

> **딕셔너리 키, 값 스왑, 값으로 키 찾기**
> 
> ```python
> dictionary = {1: 3, 2: 2}
> swap_dict = dict(map(reversed, dictionary.items()))
> ```

> **최빈 값, 빈도 상위 k개를 갖는 딕셔너리**
> 
> ```python
> import collections
> k = 1
> strs = ['a', 'a', 'b', 'c', 'd']
> value = collections.Counter(strs).most_common(k)
> ```
### 6. Graph (~370p)
> **2차원 리스트에서 값의 위치 찾기**
> 
> ```python
> strs = [['a', 'b'], ['c', 'd']]
> n = len(strs)     # 행
> m = len(strs[0])  # 열
> positions = [(i, j) for i in range(n) for j in range (m) if strs[i][j] == 'c']
> ```

> 리스트 참조 없이 **깊은 복사**
> 
> ```python
> strs = ['a', 'b', 'c']
> new_strs = strs[:] # 2차원 배열에서는 얕은 복사됨
> ```

> **중복 리스트 요소 제거**
> 
> ```python
> lists = [[1, 2], [2, 1], [3, 3, 3], [2, 1]]
> unique_ints = [list(item) for item in {tuple(sorted(list)) for list in lists}]
> ```

> **2차원 리스트에서 열 추출**
> 
> ```python
> lists = [
>     [0, 1],
>     [2, 3],
>     [4, 5],
>     [6, 7],
>     [8, 9],
> ]
> column = [e[k] for e in lists] # k 번째 열
> ```

> **리스트에서 값의 인덱스를 모두 찾기**
> 
> ```python
> strs = ['a', 'a', 'b', 'c', 'd']
> index = list(filter(lambda x: strs[x] == 'a', range(len(strs))))
> 
> lists = [
>     [0, 1],
>     [2, 3],
>     [4, 5],
>     [6, 7],
>     [8, 9],
> ]
> index = list(filter(lambda x: lists[x][0] == 2, range(len(lists)))) # 1 번째 열에서 찾기
> ```
### 7. Shortest path problem (~382p)
### 8. Tree (~445p)
> **순열**
> 
> ```python
> import itertools
> lists = [1, 2, 3, 4]
> tuple_list = itertools.permutations(lists)
> list_list = map(list, itertools.permutations(lists))
> ```

> **`==`, `is`의 차이**
> 
> ```python
> print(3 == 3.0) # return True
> print(3 is 3.0) # return False
> ```

> **`is`의 용례**
> 
> ```python
> a = 3
> print(a is None)
> print(a is True)
> print(a is False)
> ```

### 17. Sorting (~514p)
> 행렬의 **연결 연산** 및 **중첩 리스트 생성**
> 
> ```python
> a = [1]
> b = [2, 3]
> a += b 
> # 결과 : [1, 2, 3]
> 
> c = [1]
> d = [2, 3]
> c += d,
> # 결과 : [1, [2, 3]]
> 
> e = [1]
> f = [2, 3]
> e += [f]
> # 결과 : [1, [2, 3]]
> ```

> Mutable 객체의 **완전한 깊은 복사**
> 
> ```python
> import copy
> arr1 = [[1, 3], 3, 1]
> arr2 = copy.deepcopy(arr1)
> ```

> **딕셔너리의 값을 기본적으로 리스트**로 하는 방법
> 
> ```python
> import collections
> list_pair = collections.defaultdict(list)
> list_pair['key'].append(3)
> list_pair['key'].append(7)
> 
> pair = {}
> pair['key'] = [3] # 바로 append 불가능
> pair['key'].append(7)
> ```

> **딕셔너리 오름차순 키 정렬**
> 
> ```python
> pair = {'apple' : 7, 'banana' : 4}
> sorted_pair = dict(sorted(pair.items()))
> ```

> **딕셔너리 내림차순 키 정렬**
> 
> ```python
> pair = {'apple' : 7, 'banana' : 4}
> sorted_pair = dict(sorted(pair.items(), reverse=True))
> ```

> **딕셔너리 오름차순 값 정렬**
> 
> ```python
> pair = {'apple' : 7, 'banana' : 4}
> sorted_pair = dict(sorted(pair.items(), key= lambda x : x[1]))
> ```

> **딕셔너리 내림차순 값 정렬**
> 
> ```python
> pair = {'apple' : 7, 'banana' : 4}
> sorted_pair = dict(sorted(pair.items(), key= lambda x : x[1], reverse=True))
> ```

### 18. Binary Search (~540p)
> **오버플로우를 고려한 중앙 값 계산** (파이썬은 관계없음)
> + 
> ```python
> left = 5
> right = 10
> # 오버플로우 발생 가능성 존재
> mid = (left + right) // 2 
> # 오버플로우 방지
> mid = left + ((right - left) // 2)
> ```

### 19. Bits Manipulation (~568p)
> **2의 보수**
> 
> ```python
> ~ True # return -2 (Not x == -x -1)
> ```

> **2진수 10진수 상호 변환**
> 
> ```python
> print(bin(87))              # return 0b1010111
> print(int('0b1010111', 2))  # return 87
> print(int('1010111', 2))    # return 87
> ```

### 20. Sliding Window (~584p)
> 리스트 중복 값의 **인덱스 모두 찾기**
> 
> ```python
> strs = ['a', 'b', 'a', 'a']
> strs.index('a') 
> # return only 0
> list(filter(lambda x : strs[x] == 'a', range(len(strs)))) 
> # return [0, 2, 3]
> ```

> 문자열의 일부 또는 전체를 순회하며 등장횟수를 **카운트해나가면서** 최빈값을 확인
> 
> ```python
> strs = 'abaa'
> counts = collections.Counter()
> for i in range(len(strs)):
>     counts[strs[i]] += 1
>     counts.most_common()[0] 
> ```

**[home](./README.md)**