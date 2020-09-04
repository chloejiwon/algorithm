# Partition Labels

## Solution 1 - 99.73%

주어진 hint 는 sneak peek하긴 했으나 내 힘으로 99.73 가서 기분이 좋다 😎걀걀걀 

아이디어는 간단(?)하다.

1. S를 한번 훑으면서 각 원소의 가장 마지막 자릿수를 dictionary에 저장한다.
1. S[ i ]의 last idx가 지금 현재 i가 아니면, 앞에 더 있으며, 한 파티션이 거기까지는 최소한 되어야 한단 소리므로 end = dic [S [ i ]]로 한다.
1. i부터 end까지, 현재 파티션에 속한 문자 중에 end보다 더 뒤에 똑같은 문자가 있는 지 확인. 있다면 end갱신.
1. i~end까지 다 돌았으면, 한 파티션은 확정된거니까 end - i 를 리스트에 append한다.

### TimeComplexity : O(N*N) (긴가민가..)

```python
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if S == None:
            return []
        
        # 각 alphabet에 해당하는 마지막 자릿수를 저장하자.
        dic = {}
        for idx, s in enumerate(S):
            dic[s] = idx
            
        res = []
        idx = 0
        while idx < len(S):
            end = idx + 1
            s = S[idx]
            if dic[s] > idx:
                end = dic[s] + 1
            i = idx
            while i < end:
                if dic[S[i]] >= end :
                    end = dic[S[i]] + 1
                i+=1
            res.append(end - idx )
            if end == idx +1:
                idx+=1
            else:
                idx = end
                
        return res
```