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
> strs = ['a', 'a', 'b', 'c', 'd']
> value = collections.Counter(strs).most_common()[0][0]
> count = collections.Counter(strs).most_common()[0][1]
> ```
