[프로그래머스 코딩테스트 고득점 kit 풀이](https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit)

## 정렬
1. K번째 수  
```python
def cut(array, command):
    cutted_array = array[command[0] - 1:(command[1])]
    
    cutted_array.sort()
    
    return cutted_array[command[2] - 1]

def solution(array, commands):
    answer = []
    
    for command in commands:
        answer.append(cut(array, command))
    
    return answer
```

2. 가장 큰 수
```python
import functools

def comparator(a, b):
    t1 = a + b
    t2 = b + a
        
    return ((t1 < t2) - (t1 > t2))

def solution(numbers):
    
    strs = [str(number) for number in numbers]
    
    sorted_strs = sorted(strs, key=functools.cmp_to_key(comparator))
    
    return str(int(''.join(sorted_strs)))
```

3. H-Index
```python
def solution(citations):
    
    result = 0
    
    citations.sort()
    
    length = len(citations)

    for i in range (0, length + 1):
        bowl = [citation for citation in citations if citation >= i]
        if len(bowl) >= i:
            result = i

    return result
```

## 해시
1. 폰켓몬
```python
def solution(nums):
    
    length = int(len(nums) / 2)
    
    nums = list(set(nums))
    
    if length >= len(nums):
        return len(nums)
    
    else:
        return length
```

2. 완주하지 못한 선수
```python
def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for i in range (0, len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[-1]

```

3. 전화번호 목록
```python
def solution(phone_book):
    
    phone_book.sort()
    
    for i in range (0, len(phone_book) - 1):
        
        standard = phone_book[i]
        target = phone_book[i + 1]
        splitted_target = [char for char in target]
        string_taget = ''.join(splitted_target[0:len(standard)])
        
        if standard == string_taget:
            return False

    return True
```

4. 의상 (**시간초과**)
```python
import collections
import itertools

def solution(clothes):
    
    cheating_paper = []
    total = 0
    
    closet = collections.defaultdict(list)
    
    for clothing in clothes:
        type = clothing[1]
        name = clothing[0]
        closet[type].append(name)
    
    for names in closet.values():
        cheating_paper.append(len(names))
        total += len(names)
    
    sum_2 = 0
    for choice in range (2, len(cheating_paper) + 1):
        pairs = itertools.combinations(cheating_paper, choice)
        sum_1 = 0
        
        for pair in pairs:
            sum_3 = 1
            
            for element in pair:
                sum_3 *= element
            sum_1 += sum_3

        sum_2 += sum_1
        
    return sum_2 + total
```

5. 베스트 앨범
```python
def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
```

## 스택/큐
1. 같은 숫자는 싫어
```python
def solution(arr):
    
    answer = [arr[0]]
    standard = arr[0]
    
    for element in arr:
        if element != standard:
            answer.append(element)
            standard = element
    
    return answer
```

2. 기능개발
```python
import collections
import copy

def solution(progresses, speeds):
    
    d_progresses = collections.deque(progresses)
    d_speeds = collections.deque(speeds)
    
    # 진척    
    def pass_by(progresses, speeds):
        if len(progresses) < len(speeds):
            diff = len(speeds) - len(progresses)
            for i in range(diff):
                speeds.popleft()
        
        return collections.deque([x + y for x, y in zip(progresses, speeds)])
    
    # 완성 기능 카운트 및 제거
    def is_completed(progresses):
        completed = 0
        c_progresses = copy.deepcopy(progresses)
        for progress in c_progresses:
            if progress >= 100:
                progresses.popleft()
                completed += 1
            else:
                break
                
        return completed
    
    answer = []
    
    while(len(d_progresses) > 0):
        d_progresses = pass_by(d_progresses, d_speeds)
         
        reward = is_completed(d_progresses)
        if reward > 0:
            answer.append(reward)
    
    return answer
```

3. 올바른 괄호
```python
import collections

def solution(s):
    if s == "":
        return True
    
    deque = collections.deque([char for char in s])
    stack = collections.deque()
    
    for element in deque:
        if element == "(":
            stack.append("(")
        else:
            if len(stack) > 0:
                bowl = stack.pop()
                if bowl == ")":
                    stack.append(")")
            else:
                stack.append(")")
                    
           
    if len(stack) == 0:
        return True
    return False
```

5. 다리를 지나는 트럭
```python
import collections

def solution(bridge_length, weight, truck_weights):

    base_bridge = [0] * bridge_length
    
    bridge = collections.deque(base_bridge)
    trucks = collections.deque(truck_weights)
    
    bridge.popleft()
    bridge.append(trucks[0])
    seconds = 1
    current_weight = trucks.popleft()
    
    while(current_weight != 0):
        # 하차
        current_weight -= bridge.popleft()
        
        if len(trucks) == 0:
            return seconds + bridge_length
        
        # 적재 가능 무게라면
        if current_weight + trucks[0] <= weight:
            current_weight += trucks[0]
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
            
        seconds += 1
    
    return seconds
```

6. 주식 가격
```python
def solution(prices):
    
    answer = [0] * len(prices)
    
    for start in range (0, len(prices)):
        for ing in range (start, len(prices) - 1):
            if prices[start] <= prices[ing]:
                answer[start] += 1
            else:
                break
    
    return answer
```