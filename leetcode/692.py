class Solution(object):
    def sortByOrder(a,b):
        return a[0] if a[1] == b[1] else a[1]
        
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dic = {}
        res = []
        for word in words:
            if word in dic.keys() : 
                dic[word] +=1
            else :
                dic[word] =0
        sortedDic = sorted(dic.items(), key = lambda x : (-x[1],x[0]))
        print sortedDic
        for i in range(k):
            res.append(sortedDic[i][0])
        return res


















# Solution 2 - on my own
# Using Dictionary, sort them with value and alphabetical order if values are the same
# beat 84.13%
# Learned to use lambda with sorted function 
# Time Complexity O(nLogn) : for using sort
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
	dic = {}
        for word in words:
                if word not in dic:
                        dic[word] = 0
                else :
                        dic[word]+=1
        res = sorted(dic.items(), key=lambda x:(-x[1],x[0]))
        res = res[0:k]
        word = []
        for tup in res:
                word.append(tup[0])
        return word

