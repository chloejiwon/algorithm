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
        intervals = sorted(intervals, key=lambda i:i[1])
	res,cnt,tmp = [],0,0
	end = float('-inf')
	for i in range((len(intervals))):
		if end <= intervals[i][0]:
			end = intervals[i][1]
		else :
			cnt +=1
	return cnt

arr =[[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]
print eraseOverlapIntervals(arr)

arr = [[1,100],[11,22],[1,11],[2,12]]
print eraseOverlapIntervals(arr)

arr = [[1,2],[1,2],[1,2]]
print eraseOverlapIntervals(arr)

arr = [[1,2],[2,3]]
print eraseOverlapIntervals(arr)
