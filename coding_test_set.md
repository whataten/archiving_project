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