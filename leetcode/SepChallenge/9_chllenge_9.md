# Compare Version Numbers

## Solution 1 - 87.14%

흠.. 너무 쉬운 방법으로 금방..풀리네...
다른 방법으로 한번 더 풀어보는 걸로..

1. 주어진 version1,2를 '.' 으로 split해서 리스트화 한다
1. 둘이 length가 다르다면, 짧은 곳에 0을 더해 length가 동일하게 만든다. 
1. 돌아가며 숫자 대소 비교 


### TimeComplexity : O(N)


```python
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        v2 = len(version2) 
        v1 = len(version1)
        if v1 < v2:
            version1 += [0]*(v2-v1)
        elif v1 > v2:
            version2 += [0]*(v1-v2)
            
        for i,j in zip(version1, version2):
            if int(i) < int(j):
                return -1
            elif int(i) > int(j):
                return 1
        return 0
```