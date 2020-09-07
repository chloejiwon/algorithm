# Word Pattern

## Solution 1 - 86.61%

예외 처리에 좀 신경 쓰자

dictionary 자료형 사용하면 굉장히 intuitive하고 간단하게 풀 수 있다.

### TimeComplexity : O(N)

```python
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern or not str:
            return False

        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        dic = {}
        word = {}
        for pat, s in zip(pattern, str):
            if pat in dic:
                if s != dic[pat]:
                    return False
            else:
                dic[pat] = s
                
            if s in word:
                if pat != word[s]:
                    return False
            else:
                word[s] = pat
                
        return True
```