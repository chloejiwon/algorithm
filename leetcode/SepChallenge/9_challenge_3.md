# Repeated Substring Pattern

## Solution 1 - 67.5%

와 진짜 될 것 같은데 index 너무 헷갈려서 계속 틀렸다. 🤯 

아이디어는 홀수든, 짝수든 약수(2부터..) 간격 마다 sustring 확인하는 것 

예를 들어, string의 길이가 15라면 , 처음에 5-5-5비교. 3-3-3비교 하는 식이다.

### TimeComplexity : O(N)


```python
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)
        if N <= 1:
            return False
        
        for i in range(2,N+1):
            # 0 ~ N//i의 substr이 반복된다면 return True
            if N % i == 0:
                substr = s[:N//i]
                res = True
                for j in range(N//i,N,N//i):
                    if s[j:j+N//i] != substr:
                        res = False
                        break
                if res :
                    return True
        return False
```