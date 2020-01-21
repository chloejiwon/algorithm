
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<0:
            return 0
        counter = collections.Counter(nums)
        if k==0:
            cnt = 0
            for i in counter:
                if counter[i] >= 2:
                    cnt +=1
            return cnt
        cnt = 0
        for i,j in counter.items():
            if i+k in counter:
                cnt+=1
        return cnt
