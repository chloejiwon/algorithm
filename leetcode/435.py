# 435.Non-overlapping Intervals
#class Solution(object):
#    def eraseOverlapIntervals(self, intervals):
def eraseOverlapIntervals(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
	if intervals == []:
		return 0
        intervals = sorted(intervals, key=lambda i:i[0])
	res,cnt,tmp = [],0,0
	res.append(intervals[0])
	i = 0 
	while i < (len(intervals)-1):
		if res[-1][1] > intervals[i+1][0]:
			tmp +=1
			cnt +=1
		else :
			res.append(intervals[i+1])
			tmp = 0
		if tmp > 1 :
			cnt -= 1
			tmp = 0
			res.append(intervals[i])
		else :
			i+=1	
	return cnt

arr = [[1,10],[2,3],[3,4]]
print eraseOverlapIntervals(arr)

arr = [[1,2],[1,3],[2,3],[3,4]]
print eraseOverlapIntervals(arr)

arr = [[1,2],[1,2],[1,2]]
print eraseOverlapIntervals(arr)

arr = [[1,2],[2,3]]
print eraseOverlapIntervals(arr)
