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
