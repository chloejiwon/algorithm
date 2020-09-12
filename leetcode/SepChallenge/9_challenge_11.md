# Maximum Product Subarray

## Solution 1 - 64.69%

DP table을 만든다. -가 있으므로 최소값, 최대값을 전부 신경써야 한다

* DP[i][0] 은 nums[i]를 subarray에 포함시켰을 때의 최대값
* DP[i][1] 은 nums[i]를 subarray에 포함시켰을 때의 최소값


```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        maxProduct = nums[0]
        # dp[0] : 최대값, dp[1] : 최소값
        dp = []
        
        if nums[0] > 0:
            dp.append([nums[0],0])
        else :
            dp.append([0,nums[0]])
            
        maxProduct = nums[0]
        for i,num in enumerate(nums):
            maximum = 0
            minimum = 0
            
            if i == 0:
                continue
            
            minimum = min(dp[i-1][0]*num , dp[i-1][1]*num, num)
            maximum = max(dp[i-1][0]*num , dp[i-1][1]*num, num)
            
            
            dp.append([maximum,minimum])
            
            # calculate maxProduct
            maxProduct = max(dp[i][0], maxProduct)
        
        return maxProduct
```