# Contains Duplicate 3

## Solution 1 - Time Limit Excedded

당연히 Time Limit 걸릴 줄 알았다. Brtue Force approach 로 접근 

### TimeComplexity : O(n*k)

```python
class Solution(object):
    def absoluteDiff(self, a,b):
        if a < b:
            return b-a
        else :
            return a-b
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n = len(nums)
        if n <= 0 or k < 1 or t < 0 :
            return False
        for i in range(n):
            # nums[i] ~ nums[i+k] be sorted!
            end = i+k+1
            if end >= n:
                end = n
            a = sorted(nums[i:end])
            # Let's check if any duplicates
            
            for j in range(0, end - i -1, 1 ):
                if a[j+1] - a[j] <= t:
                    return True
        return False
```

## Solution 2 - 50.73%

😤아우 어려워! 진짜 오래 걸린듯. 다음에 다시 풀어보자

핵심 idea는 dictionary. Key값은 num이고, value는 index이다. (num을 넣으면 index가 튀어나오는 ..)

**해보니까, int범위를 넘는 TC가 있어서😅(Memory Error가 뜬다) 부득이하게 나눠서 key값은 t로 사용해야겠다..**

key는 t로 나눈 몫이므로, nums[ i ] - nums[ j ] <= t 이어야 하면, 

해당 조건에 부합하는 key값은 key-1, key, key+1 이다. 

1. dictionary에 각 key값과 idx값을 담는다.
1. dictionary 길이가 1이상이면, key-1, key, key+1 의 index값과, nums[ index ]가 조건에 맞는지 확인한다.


### TimeComplexity : O(n)

```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0 :
            return False

        dic = {}
        for idx, num in enumerate(nums):
            if t == 0:
                key = num
            else : 
                key = num//t
                
            if len(dic) > 0 :
                for i in range(key-1, key + 2) :
                    if i in dic and abs(idx - dic[i]) <= k and idx != dic[i] and abs(nums[dic[i]] - num) <= t:
                        return True
            
            dic[key] = idx

        return False
```
