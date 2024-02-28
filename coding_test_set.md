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