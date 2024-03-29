# 56. Merge Intervals
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals == []:
            return []
        res = []
        
        intervals = sorted(intervals,key=lambda i:i[0])
        # go through intervals and see if they need to combine or not!
        
        isCombined = False
        for i in range(len(intervals)-1):
            # compare res[-1] & intervals[i+1]
            if isCombined == False :
                res.append(intervals[i])
            if res[-1][1] >= intervals[i+1][0] :
                # Combine The two
                res[-1][1] = max(intervals[i+1][1],res[-1][1])
                isCombined = True
            else :
                # Split Now..
                isCombined = False
        if isCombined == False :
            res.append(intervals[-1])
            
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x:x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(i[1], merged[-1][1])
            else:
                merged += [i]

        return merged
