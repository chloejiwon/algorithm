class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        counter = collections.Counter(S)
        startIdx, endIdx = 0,0
        res = []
        for s in S:
            if endIdx == (len(S)-1):
                break
            ns = S.find(s)
            ne = S.rfind(s)
            if ne == ns and ne == 0:
                res.append(1)
                continue
            if ns >= startIdx and ne <= endIdx : 
                continue
            # at least [ns : ne] is one set now..
            for j in range(ns,len(S),1):
                substr = S[j]
                endidx = S.rfind(substr)
                if endidx > ne:
                    ne = endidx
                if j >= ne :
                    break
            # at least [ns : ne] is one set now..
            res.append(ne-ns+1)
            startIdx,endIdx = ns,ne
        return res
