# TimeComplexty: O(n) becaseu every element of nums pop/pushed in the queue at most once
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        def add_q(idx):
            while q and nums[q[-1]] <= nums[idx]:
                q.pop()
            q.append(idx)
            return
        
        r = []
        
        for i in range(k):
            add_q(i)
        r.append(nums[q[0]])
        
        for i in range(k, len(nums)):
            add_q(i)
            while q[0] < (i-(k-1)):
                q.popleft()
            r.append(nums[q[0]])
            
        return r
