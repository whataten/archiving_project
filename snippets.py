# 2차원 배열 ['1, B', '2, A']에서 두 번째 요소(알파벳)순으로 정렬
strs = ['1, B', '2, A']
strs.sort(key=lambda x: (x.split()[1:], x.split()[:1]))

# 문자열에 숫자와 문자만 남기기
strs = 'A man, a plan, a canal: Panama'
for s in strs:
    if s.isalnum():
        pass
    
# 리스트로 단어 골라내기
strs = ['a', 'b', 'c', 'd']
banned = ['a']
result = [word for word in strs if word not in banned]

# 리스트 요소 중 최빈 값, 빈도 찾기
import collections
strs = ['a', 'a', 'b', 'c', 'd']
value = collections.Counter(strs).most_common()[0][0]
count = collections.Counter(strs).most_common()[0][1]

# 원본 리스트 정렬, 원본 리스트 유지하며 정렬
strs = ['1', '3', '2']
strs.sort()
sorted_strs = sorted(strs)

# 리스트에서 중복 값 삭제
strs = ['1', '3', '3']
list(set(strs))

# 최댓값 최솟값 지정
import sys
mx = -sys.maxsize
mn = sys.maxsize
mx = float('inf')
mn = float('-inf')

# 데크
import collections
strs = collections.deque()
strs.append('a')
strs.appendleft('a')
strs.pop()
strs.popleft()

# 리스트를 문자열로
strs = ['a', 'b', 'c']
''.join(word for word in strs)
''.join(strs)

# 스왑
a = 1
b = 2
a, b = b, a

# 리스트 기본값 설정
T = [1, 2, 3, 4]
strs = ['기본값'] * len(T)

# 우선순위 큐
import heapq
heap = []
heapq.heappush(heap, (1, 'b'))
heapq.heappop(heap)

# 최대 힙 구현하기
import heapq
heap = [1, 3, 5, 7, 9]
max_heap = []
for item in heap:
    heapq.heappush(max_heap, (-item, item))

# 딕셔너리로 개수 확인
dic = {}
strs = ['a', 'a', 'b']
for word in strs:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
        
# 딕셔너리 키, 값 스왑, 값으로 키 찾기
dictionary = {1: 3, 2: 2}
swap_dict = dict(map(reversed, dictionary.items()))

# 최빈 값, 빈도 상위 k개를 갖는 딕셔너리
import collections
k = 1
strs = ['a', 'a', 'b', 'c', 'd']
value = collections.Counter(strs).most_common(k)

# 2차원 리스트에서 값의 위치 찾기
strs = [['a', 'b'], ['c', 'd']]
n = len(strs) # 행
m = len(strs[0]) # 열
positions = [(i, j) for i in range(n) for j in range (m) if strs[i][j] == 'c']

# 리스트 참조 없이 깊은 복사
strs = ['a', 'b', 'c']
new_strs = strs[:] # 2차원 배열에서는 얕은 복사됨

# 중복 리스트 요소 제거
lists = [[1, 2], [2, 1], [3, 3, 3], [2, 1]]
unique_ints = [list(item) for item in {tuple(sorted(list)) for list in lists}]

# 2차원 리스트에서 열 추출
lists = [
    [0, 1],
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
]
column = [e[k] for e in lists] # k 번째 열

# 리스트에서 값의 인덱스를 모두 찾기
strs = ['a', 'a', 'b', 'c', 'd']
index = list(filter(lambda x: strs[x] == 'a', range(len(strs))))

lists = [
    [0, 1],
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
]
index = list(filter(lambda x: lists[x][0] == 2, range(len(lists)))) # 1 번째 열에서 찾기

# 순열
import itertools
lists = [1, 2, 3, 4]
tuple_list = itertools.permutations(lists)
list_list = map(list, itertools.permutations(lists))

# 행렬의 연결 연산 및 중첩 리스트 생성
a = [1]
b = [2, 3]
a += b 
# 결과 : [1, 2, 3]
c = [1]
d = [2, 3]
c += d,
# 결과 : [1, [2, 3]]
e = [1]
f = [2, 3]
e += [f]
# 결과 : [1, [2, 3]]

# ==, is의 차이
print(3 == 3.0) # return True
print(3 is 3.0) # return False

# is의 용례
a = 3
print(a is None)
print(a is True)
print(a is False)

# Mutable 객체의 완전한 깊은 복사
import copy
arr1 = [[1, 3], 3, 1]
arr2 = copy.deepcopy(arr1)

# 딕셔너리의 값을 기본적으로 리스트로 하는 방법
import collections
list_pair = collections.defaultdict(list)
list_pair['key'].append(3)
list_pair['key'].append(7)

pair = collections.defaultdict() # pair = {}
pair['key'] = [3]
pair['key'].append(7)

# 딕셔너리 오름차순 키 정렬
pair = {'apple' : 7, 'banana' : 4}
sorted_pair = dict(sorted(pair.items()))

# 딕셔너리 내림차순 키 정렬
pair = {'apple' : 7, 'banana' : 4}
sorted_pair = dict(sorted(pair.items(), reverse=True))

# 딕셔너리 오름차순 값 정렬
pair = {'apple' : 7, 'banana' : 4}
sorted_pair = dict(sorted(pair.items(), key= lambda x : x[1]))

# 딕셔너리 내림차순 값 정렬
pair = {'apple' : 7, 'banana' : 4}
sorted_pair = dict(sorted(pair.items(), key= lambda x : x[1], reverse=True))

# 오버플로우를 고려한 중앙 값 계산 (파이썬은 관계없음)
left = 5
right = 10
mid = (left + right) // 2           # 오버플로우 발생 가능성 존재
mid = left + ((right - left) // 2)  # 오버플로우 방지

# 2의 보수
~ True # return -2 (Not x == -x -1)

# 2진수 10진수 상호 변환
print(bin(87))              # return 0b1010111
print(int('0b1010111', 2))  # return 87
print(int('1010111', 2))    # return 87

# 리스트 중복 값의 인덱스 모두 찾기
strs = ['a', 'b', 'a', 'a']
strs.index('a') # return only 0
list(filter(lambda x : strs[x] == 'a', range(len(strs)))) # return [0, 2, 3]

# 문자열의 일부 또는 전체를 순회하며 등장횟수를 카운트해나가면서 최빈값을 확인
strs = 'abaa'
counts = collections.Counter()
for i in range(len(strs)):
    counts[strs[i]] += 1

counts.most_common()[0] 
# return ('a', 3)

# 리스트 병합
strs_1 = ['a', 'b', 'c']
strs_2 = ['d', 'e', 'f']

strs_1.append(strs_2) 
# return ['a', 'b', 'c', ['d', 'e', 'f']]

strs_1.extend(strs_2)
strs_1 + strs_2
# return ['a', 'b', 'c', 'd', 'e', 'f']

# 복잡한 조건을 가진 정렬
import functools

def comparator(a, b):
    if len(a) > len(b):
        return 1
    else:
        return -1

strs = ['a', 'aaa', 'aa', 'aaaaaaa']
sorted_strs = sorted(strs, key=functools.cmp_to_key(comparator))
# return ['a', 'aa', 'aaa', 'aaaaaaa']

# 문자열의 문자를 원소로 하는 리스트 생성
chars = 'target'
char_list = [char for char in chars]
# return ['t', 'a', 'r', 'g', 'e', 't']

# 리스트의 모든 요소의 합
ints = [1, 2, 3, 4]
sum = sum(ints)
# return 10

# 리스트의 짝수 인덱스만 슬라이싱
ints = [1, 2, 3, 4]
ints[0::2]
# return [1, 3]

# 리스트의 홀수 인덱스만 슬라이싱
ints = [1, 2, 3, 4]
ints[1::2]
# return [2, 4]

# 소수 유무 확인
import math
def isprime(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, math.sqrt(num) + 1):
        if num % i == 0:
            return False
    
    return True