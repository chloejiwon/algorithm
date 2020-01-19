class Solution(object):
	def splitListToParts(self,root,k):
		curr ,length = root,0
		while curr:
			curr,length = curr.next, length+1
		
		each_size = length / k
		longer_parts = length % k 
		res = [each_size+1] * longer_parts + [each_size] *(k-longer_parts)
		print res
		return res
