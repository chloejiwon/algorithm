def merge( intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals == []:
            return []
        intervals = sorted(intervals,key=lambda i:i[0])
        # go through intervals and see if they need to combine or not!
        res= []
        res.append(intervals[0])
        print res[-1][0],res[-1][1]
        for i in range(len(intervals)-1):
            if res[-1][1] >= intervals[i+1][1]:
                res[-1][1] = max(intervals[i+1][1],res[-1][1])
            else :
                res.append(intervals[i])
        return res

arr = [[1,3],[2,6],[8,10],[15,18]]
arr = merge(arr)
print arr
