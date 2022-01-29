class Solution:
    def rob(self, nums: List[int]) -> int:
        a = [nums[0]]
        b = [0]
        N = len(nums)
        for i in range(1, N):
            a.append(b[i-1]+nums[i])
            b.append(max(a[i-1], b[i-1]))
        return max(a[N-1], b[N-1])
