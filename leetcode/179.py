class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # return true if "ab" > "ba"
        def larger(a, b):
            return str(a) + str(b) >= str(b) + str(a)
            
        idx = -1
        res = []
        
        for i, num in enumerate(nums):
            if i==0:
                res.append(num)
                continue
            
            loc=0
            insert = False
            for j in res:
                # insert num before j
                if not larger(j, num):
                    insert=True
                    break
                loc+=1
            
            if insert:
                # insert num before res[loc]
                res.append(-1)
                n = len(res)
                for j in range(n-1, loc, -1):
                    res[j] = res[j-1]
                res[loc]=num
            else:
                res.append(num)
        
        s = ""
        for r in res:
            s += str(r)
        return str(int(s))


# simpler version
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # return true if "ab" > "ba"
        def larger(a, b):
            return str(a) + str(b) >= str(b) + str(a)
        
        for i in range(1, len(nums)):
            j = i
            while j > 0 and larger(nums[j], nums[j-1]):
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j-=1
        
        return str(int(''.join(map(str, nums))))
